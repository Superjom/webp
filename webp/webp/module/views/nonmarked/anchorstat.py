# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 25, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
import os
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect

from webp.utils.db import DB
from webp.utils import strtpl, Util, debug_print, _debug_print
import webp.utils.users as user_utils
from webp.utils.module.anchorstat import AnchorStat as AnchorStatCtrl
from webp.utils import filetool
from webp.utils.objects.ShowEntity import ShowEntity
from webp.utils.objects.Tac import Tac

def index(request):
    dic = user_utils.user_info_context(request)
    if not dic: return redirect('/login')
    user = dic['user']

    module = user.get_module('nonmarked')
    func = module.get_func('anchorstat')
    dic.update({
        'module_flag': module.flag,
        'func_flag': func.flag,
        'purview_has_create': 'create' in func.purview,
        })

    return render_to_response("html/nonmarked/anchorstat/anchorstat_index.html", dic)


def list(request):
    tac_name = request.GET['tac_name']
    func_flag = request.GET['func_flag']
    _list = AnchorStatCtrl.search(tac_name, func_flag)
    dic = user_utils.user_info_context(request)

    user = dic['user']
    module = user.get_module('nonmarked')
    func = module.get_func('anchorstat')

    dic.update({
        'list': _list,
        'func': func,
        })
    return render_to_response("html/nonmarked/anchorstat/anchorstat_list.html", dic)


def show(request):
    db = DB()
    dic = user_utils.user_info_context(request)
    module_flag = request.GET['module_flag']
    func_flag = request.GET['func_flag']
    func_tac_id = request.GET['func_tac_id']
    sql = strtpl("select c.name from func_tac_rel a,func b,tac c where a.func_id=b.id and a.taca_id=c.id and a.id=$func_tac_id").substitute(func_tac_id = func_tac_id)
    db.execute(sql)
    tac_name = db.fetchone()[0]

    try:
        des_path = os.path.join(
                Util.INVLINK_HOME,
                module_flag, func_flag,
                'display', tac_name, 'description')

        _debug_print("des_path: " + des_path)

        description = filetool.read(des_path)
        dic['description'] = description
    except:
        pass

    try:
        more_path = os.path.join(
                Util.INVLINK_HOME, module_flag,
                func_flag, 'display', tac_name, 'more')

        _debug_print("more_path: " + more_path)

        more = filetool.read(more_path)
        dic['more'] = more
    except: 
        pass

    data = []
    try:
        k = 1
        while True:
            info = []
            info = filetool.readlines(
                os.path.join(
                    Util.INVLINK_HOME,
                    module_flag, func_flag,
                    'display', tac_name,
                    'info_%d' % k))
            try:
                de = filetool.read( os.path.join(
                        Util.INVLINK_HOME, module_flag,
                        func_flag, 'display', tac_name,
                            'description_%d' % k
                    ))
            except:
                pass

            try:
                mo = filetool.read(os.path.join(
                    Util.INVLINK_HOME,
                    module_flag, func_flag,
                    'display', tac_name,
                    'more_%d' % k
                    ))
            except:
                pass
            data.append(
                    ShowEntity(de, mo, info)
                )
            k += 1
    except:
        pass

    return render_to_response("html/nonmarked/anchorstat/anchorstat_show.html", dic)


def createinit(request):
    module_flag = request.GET['module_flag']
    db = DB()
    module_id = db.get_value("select id from module where flag='%s'" % module_flag)
    db.execute("select id,name from tac where module_id=%d" % module_id)
    res = db.fetchall()
    _list = []

    for id, name in res:
        tac = Tac(id=id, name=name)
        _list.append(tac)

    dic = user_utils.user_info_context(request)
    dic['tacs'] = _list

    return render_to_response("html/nonmarked/anchorstat/anchorstat_create.html", dic)


def create(request):
    db = DB()
    dic = user_utils.user_info_context(request)
    user = dic['user']
    module_flag = request.GET['module_flag']
    func_flag = request.GET['func_flag']
    tac_id = int(request.GET['tac_id'])
    func_id = db.get_value("select id from func where flag='%s'" % func_flag)

    count = db.get_value("select count(*) from func_tac_rel where func_id=%d and taca_id=%d" % (func_id, tac_id))

    if count > 0:
        return HttpResponse("该策略任务已经存在")

    sql = "select id,name,key_1,value_1,key_2,value_2,key_3,value_3,key_4,value_4,key_5,value_5 from tac where id=%d" % tac_id
    _debug_print(sql)
    db.execute(sql)

    res = db.fetchone()
    tac = Tac()
    if res:
        (id, name, key_1, value_1, 
            key_2, value_2, key_3, value_3, 
            key_4, value_4, key_5, value_5) = res

        for (key, value) in [
                (key_1, value_1),
                (key_2, value_2),
                (key_3, value_3),
                (key_4, value_4),
                (key_5, value_5),]:
            key = key.strip()
            value = value.strip()
            if  key or value:
                tac.map[key] = value

    sql = "insert into func_tac_rel(func_id,taca_id,user_id,status) values(%d,%d,%d,0)" % (func_id, tac_id, user.id)
    _debug_print(sql)
    db.execute(sql)
    db.commit()

    sql = "select id from func_tac_rel where tacb_id is null and func_id=%d and taca_id=%d" % (func_id, tac_id)
    _debug_print(sql)
    func_tac_id = db.get_value(sql)

    log_path = os.path.join(Util.INVLINK_HOME, module_flag,
        func_flag, "log", "%s_%s.log" % (tac.name, Util.get_date() ))

    sql = "insert into func_tac_log(func_tac_id,path,kind) values(%d,'%s',1)" % (func_tac_id, log_path) 
    _debug_print(sql)
    db.execute(sql)
    db.commit()

    shell = [
        os.path.join(Util.INVLINK_HOME,
            module_flag, "%s.sh" % func_flag),
        "-e",  Util.INVLINK_HOME,
        "-m", module_flag,
        "-f", func_flag,
        "-n", tac.name, 
        ]
    keys = ""
    values = ""

    for key,value in tac.map.items():
        keys += key + "|"
        values += value + "|"

    if keys: keys = keys[:-1] 
    if values: values = values[:-1]

    shell += ["-k", keys, "-v", values, "-l", log_path, "-t", '1']


    try:
        shell = " ".join(shell)
        _debug_print('shell '+ shell)
        output = os.popen(shell).read()
        _debug_print('output ' + output)

    except Exception, e:

        _debug_print('e: ' + e)
        sql = "update func_tac_rel set status=-1,description='Interface error' where id=%d" % func_tac_id
        _debug_print(sql)
        db.execute(sql)
        db.commit()

    return HttpResponse("1")


def create_schedule(request):
    db = DB()
    func_tac_id = int(request.GET["func_tac_id"])
    db.execute("select a.path,c.name taca_name,d.name tacb_name from func_tac_log a join func_tac_rel b on a.func_tac_id=b.id left join tac c on b.taca_id=c.id left join tac d on b.tacb_id=d.id where b.id=%d" % func_tac_id)
    res = db.fetchone()
    if res: log_path, taca_name, tacb_name = res
    dic = user_utils.user_info_context(request)
    try:
        dic.update( dict(
            schedule = filetool.read(log_path) + "<br/>",
            tacName = "%s_%s"%(taca_name, tacb_name) if tacb_name != None else taca_name,
            ))
        return render_to_response("/html/nonmarked/anchorstat/anchorstat_createschedule.html", dic)

    except:
        return HttpResponse("日志文件不存在")


def delete(request):
    db = DB()
    module_flag = request.GET["module_flag"]
    func_flag = request.GET["func_flag"]
    func_tac_id = int(request.GET["func_tac_id"])
    db.execute("select id,name,key_1,value_1,key_2,value_2,key_3,value_3,key_4,value_4,key_5,value_5 from tac where id=(select taca_id from func_tac_rel where id=%d)" % func_tac_id)
    res = db.fetchone()
    tac = Tac()

    if res:
        (id, name, 
            key_1, value_1,
            key_2, value_2,
            key_3, value_3,
            key_4, value_4,
            key_5, value_5,) = res

        tac = Tac( id = id, name = name)

        for (key, value) in [
                (key_1, value_1),
                (key_2, value_2),
                (key_3, value_3),
                (key_4, value_4),
                (key_5, value_5),]:

            if key or value:
                tac.map[key] = value
    db.execute("delete from func_tac_rel where id=%d" % func_tac_id)
    db.commit()

    log_path = os.path.join(
        Util.INVLINK_HOME, 
        module_flag,
        func_flag,
        "log",
        "%s_%s.log" % (tac.name, Util.get_date() ),
        )

    db.execute("insert into func_tac_log(func_tac_id,path,kind) values(%d,'%s',0)" % (func_tac_id, log_path))
    db.commit()

    shell = [
        os.path.join(Util.INVLINK_HOME, module_flag, 
                func_flag, "%s.sh"%func_flag),
        "-e", Util.INVLINK_HOME,
        "-m", module_flag,
        "-f", func_flag,
        "-n", tac.name,
        ]
    keys = ""
    values = ""

    for key,value in tac.map.items():
        keys += key + "|"
        values += value + "|"
    if keys: keys = keys[:-1]
    if values: values = values[:-1]

    shell += [
        "-k", keys,
        "-v", values,
        "-l", log_path,
        "-t", "2",
        ]
    try:
        shell = ' '.join(shell)
        output = os.popen(shell).read()
    except:
        db.execute("update func_tac_rel set status=-1,description='Interface error' where id=%d" % func_tac_id)
        db.commit()

    return HttpResponse("1")







if __name__ == "__main__":
    pass


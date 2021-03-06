# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 25, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
import sys
reload(sys);
# using exec to set the encoding, to avoid error in IDE.
exec("sys.setdefaultencoding('utf-8')");

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
from webp.utils.module.shell import Shell
import webp.utils.users as user_utils
from webp.utils import filetool
from webp.utils.objects.ShowEntity import ShowEntity
from webp.utils.objects.Tac import Tac
from webp.utils.objects.FuncTac import FuncTac


def index(request):
    dic = user_utils.user_info_context(request)
    if not dic: return redirect('/login')
    user = dic['user']

    module = user.get_module('nonmarked')
    func = module.get_func('googlepr')
    dic.update({
        'module_flag': module.flag,
        'func_flag': func.flag,
        'purview_has_create': 'create' in func.purview,
        'func': func,
        })

    return render_to_response("html/nonmarked/googlepr/index.html", dic)


def list(request):
    db = DB()
    tac_name = request.GET['tac_name']
    func_flag = request.GET['func_flag']
    sql = strtpl("select a.id,c.name taca_name,d.name tacb_name,e.name user_name,a.dt,a.status,a.description from func_tac_rel a left join func b on a.func_id=b.id left join tac c on a.taca_id=c.id left join tac d on a.tacb_id=d.id left join user e on a.user_id=e.id where b.flag='$func_flag' and (c.name like '%$tac_name%' or d.name like '%$tac_name%') order by a.dt desc"
        ).substitute(
            tac_name = tac_name,
            func_flag = func_flag)

    _debug_print('sql ' + sql)
    db.execute(sql)
    _list = []
    res = db.fetchall()
    _debug_print( 'res'+ str(res))
    data = {}
    for data['id'], data['taca_name'], data['tacb_name'], \
            data['user_name'], data['dt'], data['status'], data['description'] in res:

        _debug_print('data:' + str(data))
        ft = FuncTac( **data )
        _list.append(ft)
        data = {}

    dic = user_utils.user_info_context(request)

    user = dic['user']
    module = user.get_module('nonmarked')
    func = module.get_func('googlepr')

    dic.update({
        'func': func,
        'list': _list,
        })
    return render_to_response("html/nonmarked/googlepr/list.html", dic)


def show(request):
    module_flag = request.GET['module_flag']
    func_flag = request.GET['func_flag']
    func_tac_id = request.GET['func_tac_id']
    dic = user_utils.user_info_context(request)

    db = DB()
    sql = strtpl("select c.name taca_name,d.name tacb_name from func_tac_rel a join func b on a.func_id=b.id join tac c on a.taca_id=c.id left join tac d on a.tacb_id=d.id where a.id=$func_tac_id").substitute(func_tac_id = func_tac_id)
    db.execute(sql)
    taca_name, tacb_name = db.fetchone()
    tac_name = taca_name
    if tacb_name:
        tac_name += "_" + tacb_name

    try:
        des_path = os.path.join(
                Util.INVLINK_HOME,
                module_flag, func_flag,
                'display', tac_name, 'description')

        _debug_print("des_path: " + des_path)

        description = filetool.read(des_path)
        dic.update(description = description)

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
    dic['data'] = data
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

    return render_to_response("html/nonmarked/googlepr/show.html", dic)


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

    return render_to_response("html/nonmarked/googlepr/create.html", dic)


def create(request):
    db = DB()
    dic = user_utils.user_info_context(request)
    user = dic['user']
    module_flag = request.GET['module_flag']
    func_flag = request.GET['func_flag']
    taca_id = int(request.GET['taca_id'])
    try:
        tacb_id = int(request.GET['tacb_id'])
    except:
        tacb_id = 0

    func_id = db.get_value("select id from func where flag='%s'" % func_flag)

    count = db.get_value("select count(*) from func_tac_rel where func_id=%d and taca_id=%d and tacb_id=%d" % (func_id, taca_id, tacb_id))

    if count > 0:
        return HttpResponse("该策略任务已经存在")

    taca = Tac.from_db(taca_id)
    tacb = Tac.from_db(tacb_id) if tacb_id != 0 else None

    if tacb_id != 0:
        count = db.get_value("select count(*) from func_tac_rel where func_id=$func_id and taca_id in ($taca_id,$tacb_id) and status=1 and tacb_id is null")
        if count < 2: return HttpResponse("单个策略的统计数据尚未生成")
        sql = "insert into func_tac_rel(func_id,taca_id,tacb_id,user_id,status) values(%d,%d,%d,%d,0)" % (func_id, taca_id, tacb_id, user.id)

    else:
        sql = "insert into func_tac_rel(func_id,taca_id,user_id,status) values(%d,%d,%d,0)" % (func_id, taca_id, user.id)

    _debug_print("sql: " + sql)
    db.exe_commit(sql)

    tac_name = "%s_%s" % (taca.name, tacb.name) if tacb_id != 0 else taca.name

    sql = ("select id from func_tac_rel where func_id=%d and taca_id=%d and tacb_id=" + \
            str(tacb_id) if tacb_id != 0 else "null") % taca_id
    _debug_print(sql)
    func_tac_id = db.get_value(sql)

    shell = Shell(
        module_flag = module_flag,
        func_flag = func_flag,
        tac_name = tac_name,
        args = {
            't':1,
            }
        )

    log_path = shell.gen_log_path()

    sql = "insert into func_tac_log(func_tac_id,path,kind) values(%d,'%s',1)" % (func_tac_id, log_path) 
    _debug_print(sql)
    db.exe_commit(sql)
    # <<<<<<<<<<<<<<<<<<<<<<<
    a_keys, a_values = taca.keys_values

    args = {
        'k': a_keys, 'v': a_values,
    }

    if tacb_id != 0:
        # generate keys and values
        b_keys, b_values = tacb.keys_values
        args.update( {
            'x': b_keys,
            'y': b_values,
            })
    shell.update_args(args)

    res = shell.execute()
    if not res:
        sql = "update func_tac_rel set status=-1,description='Interface error' where id=%d" % func_tac_id
        _debug_print(sql)
        db.exe_commit(sql)
        return HttpResponse("0")
    return HttpResponse('1')


def create_schedule(request):
    db = DB()
    func_tac_id = int(request.GET["func_tac_id"])
    db.execute("select a.path,c.name taca_name,d.name tacb_name from func_tac_log a join func_tac_rel b on a.func_tac_id=b.id left join tac c on b.taca_id=c.id left join tac d on b.tacb_id=d.id where b.id=%d" % func_tac_id)
    res = db.fetchone()
    if res: log_path, taca_name, tacb_name = [p.strip() for p in res]
    dic = user_utils.user_info_context(request)
    try:
        dic.update( dict(
            schedule = filetool.read(log_path) ,
            tacName = "%s_%s"%(taca_name, tacb_name) if tacb_name != None else taca_name,
            ))
        return render_to_response("/html/nonmarked/googlepr/createschedule.html", dic)

    except:
        return HttpResponse("日志文件不存在")


def delete(request):
    module_flag = request.GET["module_flag"]
    func_flag = request.GET["func_flag"]
    func_tac_id = int(request.GET["func_tac_id"])

    db = DB()
    taca = Tac.from_db_by_func_tac_id("taca_id", func_tac_id)
    tacb = Tac.from_db_by_func_tac_id("tacb_id", func_tac_id)
    Tac.del_func_tac_rel(func_tac_id = func_tac_id)

    tac_name = "%s_%s" % (taca.name, tacb.name)

    a_keys, a_values = taca.keys_values
    b_keys, b_values = tacb.keys_values

    shell = Shell(
        module_flag = module_flag,
        func_flag = func_flag,
        tac_name = tac_name,
        args = {
            'k': a_keys, 'v': a_values,
            'x': b_keys, 'y': b_values,
            't': 2,
            }
        )

    log_path = shell.gen_log_path()

    db.exe_commit("insert into func_tac_log(func_tac_id,path,kind) values(%d,'%s',0)" % (func_tac_id, log_path))

    res = shell.execute()

    if res:
        return HttpResponse('1')
    else:
        db.exe_commit("update func_tac_rel set status=-1,description='Interface error' where id=%d" % func_tac_id)
    return HttpResponse('1')




if __name__ == "__main__":
    pass


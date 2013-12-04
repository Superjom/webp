# -*- coding: utf-8 -*-
'''
Created on Dec 23, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
from __future__ import division

import sys
reload(sys);
# using exec to set the encoding, to avoid error in IDE.
exec("sys.setdefaultencoding('utf-8')");


from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect

from webp.utils.db import DB
import webp.utils.users as user_utils
from webp.utils.module.tac import Tac as TacCtrl
from webp.utils.module.module import Module as ModuleCtrl
from webp.utils.objects.Tac import Tac

List = list


def index(request):
    dic = user_utils.user_info_context(request)
    if not dic: return redirect('/login')
    user = dic['user']

    module = user.get_module('nonmarked')
    func = module.get_func('nonmarkedtac')

    data = {
        'module_flag': module.flag,
        'func_flag': func.flag,
        'purview_has_create': 'create' in func.purview,
        }

    dic.update(data)
    return render_to_response("html/nonmarked/tac/tac_index.html", dic)


def list(request):
    tac_name = request.GET.get('tagname', '')
    module_id = ModuleCtrl.get_id(flag='nonmarked')
    res = TacCtrl.search(
            tac_id=-1,
            module_id=module_id, 
            tac_name=tac_name)
    dic = user_utils.user_info_context(request)
    user = dic['user']
    module = user.get_module('nonmarked')
    func = module.get_func('nonmarkedtac')
    dic.update({
        'list': res,
        'purview_has_update': 'update' in func.purview,
        'purview_has_delete': 'delete' in func.purview,
        })
    return render_to_response("html/nonmarked/tac/tac_list.html", dic)


def createinit(request):
    db = DB()
    dic = user_utils.user_info_context(request)
    module_flag = 'nonmarked'
    module_id = ModuleCtrl.get_id(module_flag)
    db.execute("select key_1, key_2, key_3, key_4, key_5 from tac where module_id=%d order by dt desc limit 0,1" % module_id)
    res = db.fetchall()

    if not res:
        keylist = ["" for i in range(5)]
    else:
        res = List(res[0])
        #print 'createinit res:', res
        keys = res + ["" for i in range(5)]
        keylist = [keys[i] for i in range(5)]
    dic.update({
        'keylist': keylist,
        })
    return render_to_response("html/nonmarked/tac/tac_create.html", dic)


def create(request):
    module_flag = request.GET['module_flag']
    module_id = ModuleCtrl.get_id(module_flag)
    g = request.GET.copy()
    g['module_id'] = int(module_id)
    if TacCtrl.create(g):
        return HttpResponse("1")
    return HttpResponse("0")


def updateinit(request):
    tac_id = int(request.GET['tac_id'])
    res = TacCtrl.search(tac_id = tac_id)[0]
    
    print 'updateinit res', res, len(res)

    id, name, description, dt, key_1, value_1, \
            key_2, value_2 , key_3, value_3, \
            key_4, value_4, key_5, value_5, module_name = res
    # create a new tac
    tac = Tac(
        id = id,
        name = name,
        description = description,
        dt = dt)
    for key,value in [
                (key_1, value_1,),
                (key_2, value_2,),
                (key_3, value_3,),
                (key_4, value_4,),
                (key_5, value_5,),
            ]:
        key, value = key.strip(), value.strip()
        if key and value:
            tac.map.update({key : value})
    dic = user_utils.user_info_context(request)
    dic.update(
        {'tac': tac}
    )
    return render_to_response("html/nonmarked/tac/tac_update.html", dic)

def update(request):
    tac_id = int(request.GET['tac_id'])
    dic = request.GET.copy()
    dic['tac_id'] = int(tac_id)
    if TacCtrl.update(dic):
        return HttpResponse("1")
    return HttpResponse("0")

def delete(request):
    tac_id = int(request.GET['tac_id'])
    res = TacCtrl.delete(tac_id)
    if res is True:
        return HttpResponse("1")
    return HttpResponse(res)

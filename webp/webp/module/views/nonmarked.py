# -*- coding: utf-8 -*-
'''
Created on Dec 23, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
from __future__ import division

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect

import webp.utils.users as user_utils
from webp.utils.module.tac import Tac as TacCtrl
from webp.utils.module.module import Module as ModuleCtrl

def tac_index(request):
    dic = user_utils.user_info_context(request)
    user = dic['user']
    module = user.get_module('nonmarked')
    func = module.get_func('nonmarkedtac')
    if not dic: return redirect('/login')

    data = {
        'module_flag': module.flag,
        'func_flag': func.flag,
        'purview_has_create': 'create' in func.purview,
        }

    dic.update(data)
    return render_to_response("html/nonmarked/tac/tac_index.html", dic)


def tac_list(request):
    tac_name = request.GET.get('tagname', '')
    tac_ctrl = TacCtrl()
    module_ctrl = ModuleCtrl()
    module_id = module_ctrl.get_id(flag='nonmarked')
    res = tac_ctrl.search(module_id, tac_name)

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



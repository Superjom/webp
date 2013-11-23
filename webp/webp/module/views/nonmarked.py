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
from webp.utils import pprint

def tac_index(request):
    dic = user_utils.user_info_context(request)
    if not dic: return redirect('/login')
    print 'dic', dic
    pprint(dic['user'])
    print dic['user']

    return render_to_response("html/nonmarked/tac/tac_index.html", dic)

def tac_list(request):
    return render_to_response("html/nonmarked/tac/tac_list.html")




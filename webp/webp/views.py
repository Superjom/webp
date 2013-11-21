# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 11, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response

from webp.utils.users import user_info_context

def index(request):
    user = user_info_context(request)
    return render_to_response("html/index.html", user)

def header(request):
    return render_to_response("html/header.html")

def footer(request):
    return render_to_response("html/footer.html")

def left(request):
    return render_to_response("html/left.html")

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("login.html", c)

def debug(request):
    pass





if __name__ == "__main__":
    pass


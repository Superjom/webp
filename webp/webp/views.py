# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 11, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response, redirect

import webp.utils.users as user_utils

def index(request):
    user = user_utils.user_info_context(request)
    if not user:
        return redirect('/login')
    return render_to_response("html/index.html", user)

def header(request):
    user = user_utils.user_info_context(request)
    return render_to_response("html/header.html", user)

def footer(request):
    return render_to_response("html/footer.html")

def left(request):
    user = user_utils.user_info_context(request)
    return render_to_response("html/left.html", user)

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("login.html", c)

def logout(request):
    user_utils.logout(request)
    return redirect('/login')

def debug(request):
    pass






if __name__ == "__main__":
    pass


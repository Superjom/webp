from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from webp.utils.objects.LoginInfo import LoginInfo

import webp.utils.users as users_ctrl

def login(request):
    userid = request.session.get('userid', None)
    password = request.session.get('password', None)
    
    login_info = LoginInfo()
    
    # check userid password format
    if not userid and password:
        login_info.kind = -3

        return render_to_response("./users/login.html", {'login_info': {'is_error':True, 'info':'error'}})
                        

    # search in database
    userinfo = users_ctrl.login(userid, password)
    print userinfo

    login_info.kind = -1

    return render_to_response("./users/login.html", {'login_info': {'is_error':True, 'info':'error'}})

    return render_to_response( "./users/login.html", {'login_info': login_info})

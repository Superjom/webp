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
from webp.utils.objects.LoginInfo import LoginInfo

import webp.utils.users as users_ctrl

def login(request):
    userid = request.POST.get('userid', None)
    password = request.POST.get('password', None)
    
    login_info = LoginInfo()

    context = {}
    context.update(csrf(request))
    
    # check userid password format
    if not userid and password:
        login_info.kind = -3
        context.update( {'login_info': login_info})
        return render_to_response("./login.html", context)
    # search in database
    res = users_ctrl.login(request, userid, password)
    print res
    login_info.kind = 0 if res else -1

    context.update( {'login_info': login_info})

    return render_to_response("./login.html", context)

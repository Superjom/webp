# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 11, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''

from webp.utils.objects.User import User
from webp.utils.db import DB

def user_info_context(request):
    """
    返回 userid 及 登陆框
    用于登陆
    """
    userid = request.session.get('userid', None)
    username = request.session.get('username', None)

    if not userid and username:
        return None

    user = User(userId=userid, name=username)

    return user

def login(username, password):
    """
    input username and password
    search database
    get a login User obejct

    @args:
        username
        password

    @returns:
        object of User / None
    """
    db = DB()
    db.execute(
        "select pwd,password('%s') mypwd from user where userid='%s'" % (username, password))
    res = db.fetchone()
    return res


def logout(request):
    """
    clear session of current user
    """
    raise NotImplemented







if __name__ == "__main__":
    pass


# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 11, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''

from webp.utils.objects.User import User as UserObject
from webp.utils.module import Module
from webp.utils.db import DB

class User(object):
    def __init__(self, userid):
        self.userid = userid
        self.userobject = UserObject()
        self.db = DB()

    def fill(self):
        '''
        query database and fill data
        '''
        self._fill_base_info()
        self._fill_module()

    def _fill_base_info(self):
        sql = "select a.id,a.userid,a.name,a.sex,a.role_id,b.name role_name from user a, role b where a.role_id=b.id and a.userid='%s'" % self.userid
        self.db.execute(sql)
        res = self.db.fetchone()
        print 'res:', res
        if res:
            o = self.userobject
            o.id, o.userId, o.name, o.roleId = \
                    res[0], res[1], res[2], res[4]
        #print 'user_info:', self.userobject

    def _fill_module(self):
        '''
        query database and get all modules according to 
        user's role
        '''
        roleId = self.userobject.roleId
        sql = "select a.id module_id,a.flag module_flag,a.name module_name from module a where exists (select * from func b,func_purview_role_rel c where a.id=b.module_id and b.id=c.func_id and c.role_id=%d) order by a.sequence asc,a.id desc" % roleId
        self.db.execute(sql)
        res = self.db.fetchall()

        print 'get res: ', res

        for module_id, module_flag, module_name in res:
            print '@ get module', module_id, module_flag, module_name 
            m = Module(module_id)
            m.fill(module_flag, module_name, roleId)
            module = m.get_object()
            print '@ modulename len', module_name, len(module.list)
            self.userobject.list.append(module)

    def get_object(self):
        return self.userobject

    def __str__(self):
        return str(self.userobject)


def user_info_context(request):
    """
    返回 userid 及 登陆框
    用于登陆
    """
    userobject = request.session.get('userobject', None)

    if userobject:
        return {'user' : userobject}


def login(request, userid, password):
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
        "select pwd,password('%s') mypwd from user where userid='%s'" % (password, userid))
    res = db.fetchone()

    pwd, mypwd = res if res else (None, None)

    if pwd and pwd == mypwd:
        # save user info to session
        request.session['userid'] = userid
        userobject = User(userid)
        userobject.fill()
        request.session['userobject'] = userobject.get_object()
        return True



def logout(request):
    """
    clear session of current user
    """
    if 'userid' in request.session:
        del request.session['userid']

    if 'userobject' in request.session:
        del request.session['userobject']







if __name__ == "__main__":
    pass


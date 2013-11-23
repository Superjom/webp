# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 21, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''


class User(object):

    def __init__(self, id=-1, userId="", name="",
                password="", roleId=-1, roleName="", dt="", _list=[]):

        self.id =       id
        self.userId =   userId
        self.name   =   name
        self.password = password
        self.roleId =   roleId
        self.roleName = roleName
        self.dt =       dt
        self.list =     _list

    def isAdmin(self):
        return self.roleId == 1

    def get_module(self, flag):
        for m in self.list:
            if m.flag == flag:
                return m

    def __str__(self):
        return '\n'.join([
            '<User ',
            'id: %d' % self.id,
            'userId: %s' % self.userId,
            'name: %s' % self.name,
            'roleId: %s' % self.roleId,
            'list: %s' % ' '.join([ str(m) for m in self.list]),
            '>',
        ])




if __name__ == "__main__":
    pass


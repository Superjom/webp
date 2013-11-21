# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 21, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''


class User(object):

    def __init__(self, id=-1, userId="", name="",
                password="", roleID=-1, roleName="", dt="", _list=[]):

        self.id =       id
        self.userId =   userId
        self.name   =   name
        self.password = password
        self.roleID =   roleID
        self.roleName = roleName
        self.dt =       dt
        self.list =     _list

    def isAdmin(self):
        return self.roleID == 1




if __name__ == "__main__":
    pass


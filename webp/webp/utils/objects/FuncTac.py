# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 25, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''

class FuncTac(object):
    def __init__(self, id=None, taca_name=None, tacb_name=None, user_name=None, dt=None, 
                    status=None, description=None):
        self.id = id
        self.taca_name = taca_name
        self.tacb_name = tacb_name
        self.user_name = user_name
        self.dt = dt
        self.status = status
        self.description = description

    @property
    def status_is_1(self):
        return self.status == 1

    @property
    def status_is_m1(self):
        return self.status == -1

    @property
    def status_is_0(self):
        return self.status == 0

    def __str__(self):

        return '\n'.join([
            "<uncTac "
            "   id:\t%s" % self.id,
            "   taca_name:\t%s" % self.taca_name,
            "   tacb_name:\t%s" % self.tacb_name,
            "   user_name:\t%s" % self.user_name,
            "   dt:\t%s" % self.dt,
            "   status:\t%s" % self.status,
            "   description:\t%s" % self.description,
            ">",
            ])






if __name__ == "__main__":
    pass


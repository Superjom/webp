# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 21, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''

KINDS = {
    -1 : "no user",
    -2 : "password wrong",
    -3 : "no username or password", 
    0 : "success",
}

class LoginInfo(object):
    def __init__(self, kind=100):

        self.kind = kind

    @property
    def is_success(self): 
        return self.kind == 0

    @property
    def is_error(self):
        return self.kind != 0

    @property
    def is_no_user(self):
        return self.kind == -1

    @property
    def info(self):
        if self.kind in KINDS:
            return KINDS[self.kind]
        else:
            return "system error!"

    def __str__(self):
        return "<LoginInfo: %d: %s>" % (self.kind, self.info)







if __name__ == "__main__":
    pass


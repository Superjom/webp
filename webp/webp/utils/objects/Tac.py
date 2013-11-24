# -*- coding: utf-8 -*-
'''
Created on Dec 23, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
from __future__ import division
from webp.utils import e

class Tac(object):
    def __init__(self, id=-1, name="", description="", dt="", map={}):
        self.id = id
        self.name = e(name)
        self.description = e(description)
        self.dt = dt
        self.map = map

    @property
    def map_keys(self):
        keys = list(self.map.keys())
        keys += ["" for i in range(5)]
        return keys[:5]

    @property
    def keyvalues(self):
        res = list(self.map.items())
        res += [ ("", "",) for i in range(5)]
        return res[:5]

    def __nonzero__(self):
        return self.id != -1


if __name__ == '__main__':
    t = Tac()
    t.id = 1
    print bool(t)

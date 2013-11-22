# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 21, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''

class Func(object):

    def __init__(self, id=-1, flag="", name="", purview=set()):

        self.id = id
        self.flag = flag
        self.name = name
        self.purview = purview

    def __str__(self):
        return '\n'.join([
            '<Func',
            'id: %d' % self.id,
            'flag: %s' % self.flag,
            'name: %s' % self.name,
            'purview: %s' % ' '.join(self.purview),
            '>',
            ])





if __name__ == "__main__":
    pass


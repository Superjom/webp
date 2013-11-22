# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 22, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''

class Module(object):
    """
    module of function
    """
    def __init__(self, id=-1, flag="", name=""):

        self.id = id
        self.flag = flag
        self.name = name
        self.list = []

    def __str__(self):
        return '\n'.join([
            '<Module',
            'id: %d'% self.id,
            'flag: %s' % self.flag,
            'name: %s' % self.name,
            'list: %s' % ' '.join([str(o) for o in self.list]),
            '>',

            ])





if __name__ == "__main__":
    pass


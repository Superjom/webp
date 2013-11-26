# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 25, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
def read(path):
    with open(path) as f:
        return f.read()

def readlines(path):
    with open(path) as f:
        return f.readlines()






if __name__ == "__main__":
    pass


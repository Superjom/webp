# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 25, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''

class ShowEntity(object):
    def __init__(self, de="", mo="", info=[]):
        self.de = de
        self.mo = mo
        self.info = info
        self.data = []
        self.show()

    def show(self):
        self.navigation = self.info[0].split("\t")
        for line in self.info[1:]:
            self.data.append(line.split("\t"))





if __name__ == "__main__":
    pass


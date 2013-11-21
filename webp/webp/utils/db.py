# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 21, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
from django.db import connection

class DB(object):
    def execute(self, cmd):
        self.cursor = connection.cursor()
        self.cursor.execute(cmd)

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()


if __name__ == "__main__":
    pass


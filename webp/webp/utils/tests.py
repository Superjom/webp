# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 22, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''

import unittest
from unittest import TestCase
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('../../')

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'webp.settings' 

from users import User
from module import Module

class UserTestCase(TestCase):
    def setUp(self):
        print 'testing User'
        self.user = User('admin')

    def test_fill_base_info(self):
        self.user.fill()
        #self.assertEqual(lion.speak(), 'The lion says "roar"')
        #self.assertEqual(cat.speak(), 'The cat says "meow"')
        print self.user.get_object()

class ModuleTestCase(TestCase):
    def setUp(self):
        print '-' * 200
        print 'testing Module'
        self.module = Module(1)
        self.module.fill('dcg', 'DCG', 1)
        obj = self.module.get_object()
        print obj









if __name__ == "__main__":
     unittest.main()


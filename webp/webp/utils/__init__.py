# -*- coding: utf-8 -*-
import os
from datetime import datetime as dt
import pprint as p_print
from string import Template as strtpl
import functools
from webp.settings import DEBUG

def pprint(s):
    pp = p_print.PrettyPrinter(indent=4)
    pp.pprint(s)

def e(s):
    return s.encode('utf8')

def debug():
    import os
    import sys
    path = os.path.dirname(__file__)
    path = os.path.join(path, '../../')
    sys.path.append(path)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'webp.settings' 

def debug_print(*args):
    if(DEBUG):
        print "[.. debug ..]", 
        for a in args:
            print a, 
        print

_debug_print = debug_print


def copy_dic(dic, newdic):
    for key,value in dic.items():
        newdic[key] = value

class Util(object):
    SYSTEM_HOME = os.path.join( os.path.dirname(__file__), "..")
    INVLINK_HOME = ""
    PURVIEW_LIST = []

    @staticmethod
    def set_environment():
        from webp.settings import PROJECT_PATH 
        from webp.conf import INVLINK_HOME
        Util.SYSTEM_HOME = PROJECT_PATH
        Util.INVLINK_HOME = INVLINK_HOME
        # get flags
        from db import DB
        db = DB()
        db.execute("select flag from purview")
        res = db.fetchall()
        for flag in res:
            Util.PURVIEW_LIST.append(flag)

    @staticmethod
    def get_date():
        d = dt.now()
        time = d.strftime("%Y%m%d%H%M%S")
        return time


class DictProperty(object):
    ''' Property that maps to a key in a local dict-like attribute. 
    Once visited, property will be stored and never be changed even the original property is changed.
    '''
    def __init__(self, attr, key=None, read_only=False):
        self.attr, self.key, self.read_only = attr, key, read_only

    def __call__(self, func):
        functools.update_wrapper(self, func, updated=[])
        self.getter, self.key = func, self.key or func.__name__
        return self

    def __get__(self, obj, cls):
        if obj is None: return self
        key, storage = self.key, getattr(obj, self.attr)
        if key not in storage: storage[key] = self.getter(obj)
        return storage[key]

    def __set__(self, obj, value):
        if self.read_only: raise AttributeError("Read-Only property.")
        getattr(obj, self.attr)[self.key] = value

    def __delete__(self, obj):
        if self.read_only: raise AttributeError("Read-Only property.")
        del getattr(obj, self.attr)[self.key]

if __name__ == '__main__':

    d = DictProperty({})
    d.name = 'superjom'
    print d.name








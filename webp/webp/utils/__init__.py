# -*- coding: utf-8 -*-
import os
from datetime import datetime as dt
import pprint as p_print
from string import Template as strtpl
from ConfigParser import ConfigParser
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

def debug_print(s):
    if(DEBUG):
        print "[.. debug ..]", s

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








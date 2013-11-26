# -*- coding: utf-8 -*-
import os
from datetime import datetime as dt
import pprint as p_print
from string import Template as strtpl
from ConfigParser import ConfigParser

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

def copy_dic(dic, newdic):
    for key,value in dic.items():
        newdic[key] = value

class Util(object):
    SYSTEM_HOME = ""
    INVLINK_HOME = ""
    PURVIEW_LIST = []

    @staticmethod
    def set_environment(path):
        Util.SYSTEM_HOME = path
        config_parser = ConfigParser()
        conf_path = os.path.join(Util.SYSTEM_HOME, "conf/conf.properties")
        config_parser.read(conf_path)
        Util.INVLINK_HOME = config_parser.get("INVLINK_HOME")
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








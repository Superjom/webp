# -*- coding: utf-8 -*-
import pprint as p_print

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


# -*- coding: utf-8 -*-
import pprint as p_print

def pprint(s):
    pp = p_print.PrettyPrinter(indent=4)
    pp.pprint(s)

def e(s):
    return s.encode('utf8')


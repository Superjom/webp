# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 21, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
import sys
reload(sys);
# using exec to set the encoding, to avoid error in IDE.
exec("sys.setdefaultencoding('utf-8')");

from webp.utils.objects.Module import Module as ModuleObject
from webp.utils.db import DB
from webp.utils import e

from webp.utils.objects.Func import Func

class Module(object):

    def __init__(self, id=-1):
        self.id = id
        self.moduleobject = ModuleObject()
        self.db = DB()

    def fill(self, module_flag, module_name, roleId):
        '''
        query db and get all data to fill the object
        '''
        self.moduleobject.id = self.id
        self.moduleobject.flag = module_flag
        self.moduleobject.name = module_name
        self.roleId = roleId
        self._fill_funcs()

    def get_object(self):
        return self.moduleobject

    #TODO some bugs here
    def _fill_funcs(self):
        print 'module init len', len(self.moduleobject.list)
        sql = "select a.id func_id,a.flag func_flag,a.name func_name,c.flag purview_flag from func a,func_purview_role_rel b,purview c where a.id=b.func_id and b.purview_id=c.id and a.module_id=%d and b.role_id=%d order by a.sequence asc,a.id desc" % (self.id, self.roleId)
        self.db.execute(sql)
        res = self.db.fetchall()

        func_ids = set()
        last_f = None

        print 'module res:', res

        for func_id, func_flag, func_name, purview_flag in res:
            func_flag = e(func_flag)
            func_name = e(func_name)
            purview_flag = e(func_name)

            print '@func:', func_id, func_flag, func_name, purview_flag 
            print '@func_ids', func_ids
            print '@module len', len(self.moduleobject.list)

            if func_id in func_ids:
                last_f.purview.add(purview_flag)

            else:
                func_ids.add(func_id)
                f = Func(
                    id = func_id, 
                    flag = func_flag,
                    name = func_name
                )
                f.purview.add(purview_flag)
                self.moduleobject.list.append(f)
                print 'module append len', len(self.moduleobject.list)
                last_f = f

    def __str__(self):
        return str(self.moduleobject)

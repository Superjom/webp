# -*- coding: utf-8 -*-
'''
Created on Dec 23, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
from __future__ import division
import sys
reload(sys);
# using exec to set the encoding, to avoid error in IDE.
exec("sys.setdefaultencoding('utf-8')");


#----------------- debug -------------
if __name__ == '__main__':
    import sys
    sys.path.append('/home/chunwei/webp/webp')
    from webp.utils import debug; debug()
#---------------- end  debug -------------


from webp.utils.db import DB

db = DB()

class Module(object):
    @staticmethod
    def get_id(flag):
        db = DB()
        sql = "select id from module where flag='%s'" % flag
        print 'sql:', sql
        db.execute(sql)
        res = db.fetchone()
        id = res[0]
        return id

    @staticmethod
    def create(dic):
        db = DB()
        g = dic
        module_id = g['module_id']
        sql = "insert into tac(module_id,name,description,key_1,value_1,key_2,value_2,key_3,value_3,key_4,value_4,key_5,value_5) values(%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
            % (module_id, g['name'], g['description'], 
                g['key_1'], g['value_1'], g['key_2'], g['value_2'], 
                g['key_3'], g['value_3'], g['key_4'], g['value_4'], 
                g['key_5'], g['value_5'], )
        try:
            db.execute(sql)
            return True
        except Exception,e:
            print 'error of create:', e
        return False


if __name__ == '__main__':
    Module.get_id('nonmarked')

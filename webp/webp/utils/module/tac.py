# -*- coding: utf-8 -*-
'''
Created on Dec 23, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
from __future__ import division



#----------------- debug -------------
if __name__ == '__main__':
    import sys
    sys.path.append('/home/chunwei/webp/webp')
    from webp.utils import debug; debug()
#---------------- end  debug -------------

from webp.utils.db import DB


class Tac(object):
    def __init__(self):
        self.db = DB()

    def search(self, module_id, tac_name):
        sql = " select a.id,a.name,a.description,a.dt,a.key_1,a.value_1,a.key_2,a.value_2,a.key_3,a.value_3,a.key_4,a.value_4,a.key_5,a.value_5,b.name module_name from tac a,module b where a.module_id=b.id and b.id=%d and a.name like '%s' order by a.dt desc" % (module_id, tac_name)
        print 'sql:', sql
        self.db.cursor.execute(sql)
        res = self.db.fetchall()
        print 'res:', res
        _list = []
        for id, name, description, dt, key, value, \
            key_1, value_1, key_2, value_2, key_3, value_3, \
            key_4, value_4, key_5, value_5, \
            b_name, module_name in res:
            _list.append({
                'id': id,
                'name': name,
                'description': description,
                'dt': dt,
                'key': key, 'value': value,
                'key_1': key, 'value_1': value,
                'key_2': key, 'value_2': value,
                'key_3': key, 'value_3': value,
                'key_4': key, 'value_4': value,
                'key_5': key, 'value_5': value,
                'b_name': b_name,
                'module_name': module_name,
                })
        return _list

    def insert(self, module_id, name, description, 
                key_1, value_1, key_2, value_2,
                key_3, value_3, key_4, value_4,
                key_5, value_5):
        sql = "insert into tac(module_id,name,description,key_1,value_1,key_2,value_2,key_3,value_3,key_4,value_4,key_5,value_5) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        self.db.execute(sql)

    def update(self, tac_id, name, description, 
        key1, value1, key2, value2, key3, value3, key4, value4, 
            key5, value5):
        sql = "update tac set name='%s',description='%s',key_1='%s',value_1='%s',key_2='%s',value_2='%s',key_3='%s',value_3='%s',key_4='%s',value_4='%s',key_5='%s',value_5='%s' where id='%s'" % (
        tac_id, name, description, key1, value1, key2, value2, 
        key3, value3, key4, value4, key5, value5)

        self.db.execute(sql)

    def has(self, tac_id):
        sql = "select count(*) from func_tac_rel where taca_id=" + tac_id + " or tacb_id=" + tac_id
        self.db.execute(sql)
        res = self.db.fetchone()
        print 'count', res
        count = res[0]
        return count > 0

    def delete(self, id):
        sql = "delete from tac where id=%d" % id
        self.db.execute(sql)






if __name__ == '__main__':
    from module import Module

    m = Module()
    module_id = m.get_id('nonmarked')

    tac = Tac()
    res = tac.search(module_id, 'nonmarkedtac')
    print 'res', res

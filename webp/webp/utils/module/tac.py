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

db = DB()

class Tac(object):

    @staticmethod
    def search(tac_id=-1, module_id=-1, tac_name=""):
        if tac_id != -1:
            return Tac.search_by_tac_id(tac_id=tac_id)

        elif module_id != -1:
            return Tac.search_by_module_id(module_id, tac_name)

    @staticmethod
    def search_by_tac_id(tac_id):
        db = DB()
        sql = "select a.id,a.name,a.description,a.dt,a.key_1,a.value_1,a.key_2,a.value_2,a.key_3,a.value_3,a.key_4,a.value_4,a.key_5,a.value_5,b.name module_name from tac a,module b where a.module_id=b.id and a.id=%d"  % tac_id
        #print 'search_by_tacid', sql
        db.execute(sql)
        res = db.fetchall()
        return res

    @staticmethod
    def search_by_module_id(module_id, tac_name):
        db = DB()
        if tac_name:
            sql = " select a.id,a.name,a.description,a.dt,a.key_1,a.value_1,a.key_2,a.value_2,a.key_3,a.value_3,a.key_4,a.value_4,a.key_5,a.value_5,b.name module_name from tac a,module b where a.module_id=b.id and b.id=%d and a.name like '%s' order by a.dt desc" % (module_id, tac_name)
        else:
            sql = " select a.id,a.name,a.description,a.dt,a.key_1,a.value_1,a.key_2,a.value_2,a.key_3,a.value_3,a.key_4,a.value_4,a.key_5,a.value_5,b.name module_name from tac a,module b where a.module_id=b.id and b.id=%d order by a.dt desc" % (module_id, )

        print 'search_by_module_id', sql
        db.cursor.execute(sql)
        res = db.fetchall()
        _list = []

        for id, name, description, dt, \
            key_1, value_1, key_2, value_2, key_3, value_3, \
            key_4, value_4, key_5, value_5, module_name in res:

            keyvalues = [(key, value) for (key, value) in (
                    (key_1, value_1),
                    (key_2, value_2),
                    (key_3, value_3),
                    (key_4, value_4),
                    (key_5, value_5),
                ) if key ]
            _list.append({
                'id': id,
                'name': name,
                'description': description,
                'dt': dt,
                'keyvalues': keyvalues,
                'module_name': module_name,
                })
        return _list

    @staticmethod
    def create(dic):
        db = DB()
        keys = tuple([ dic[key] for key in ('module_id', 'name', 'description', 
                'key_1', 'value_1', 'key_2', 'value_2',
                'key_3', 'value_3', 'key_4', 'value_4',
                'key_5', 'value_5',) ])
        #keys = (2, "sdfa", 'sdfsad', '', '', '', '', '', '', '', '', '', '')

        sql = "insert into tac(module_id,name,description,key_1,value_1,key_2,value_2,key_3,value_3,key_4,value_4,key_5,value_5) values(%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % keys
        print 'create sql:', sql
        db.execute(sql)
        db.commit()
        return True

    @staticmethod
    def update(dic):
        db = DB()
        sql = "update tac set name='%s',description='%s',key_1='%s',value_1='%s',key_2='%s',value_2='%s',key_3='%s',value_3='%s',key_4='%s',value_4='%s',key_5='%s',value_5='%s' where id=%d" \
            % tuple([ dic[key] for key in (
                 'name', 'description',
                'key_1', 'value_1', 
                'key_2', 'value_2',
                'key_3', 'value_3',
                'key_4', 'value_4',
                'key_5', 'value_5',
                'tac_id',
            )])

        db.execute(sql)
        db.commit()
        return True

    @staticmethod
    def has( tac_id):
        db = DB()
        sql = "select count(*) from func_tac_rel where taca_id=%d or tacb_id=%d" % (tac_id, tac_id)
        db.execute(sql)
        res = db.fetchone()
        print 'count', res
        count = res[0]
        return count > 0

    @staticmethod
    def delete(tac_id):
        db = DB()
        if Tac.has(tac_id):
            return "a task is running!"

        sql = "delete from tac where id=%d" % tac_id
        db.execute(sql)
        db.commit()
        return True





if __name__ == '__main__':
    from module import Module

    m = Module()
    module_id = m.get_id('nonmarked')

    tac = Tac()
    res = tac.search(module_id, 'nonmarkedtac')
    print 'res', res

    

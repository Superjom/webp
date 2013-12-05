# -*- coding: utf-8 -*-
'''
Created on Dec 23, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
from __future__ import division
from webp.utils import e
from webp.utils.db import DB

class Tac(object):
    def __init__(self, id=-1, name="", description="", dt="", map={}):
        self.id = id
        self.name = e(name)
        self.description = e(description)
        self.dt = dt
        self.map = map

    @property
    def map_keys(self):
        keys = list(self.map.keys())
        keys += ["" for i in range(5)]
        return keys[:5]

    @property
    def keyvalues(self):
        res = list(self.map.items())
        res += [ ("", "",) for i in range(5)]
        return res[:5]

    @property
    def keys_values(self):
        '''
        get a string line of keys and values
        '''
        keys = ""
        values = ""
        for key,value in self.map.items():
            keys += key + "|"
            values += value + "|"

        if keys: keys = keys[:-1] 
        if values: values = values[:-1]
        return (keys, values)


    @staticmethod
    def from_db(id):
        db = DB()
        sql = "select id,name,key_1,value_1,key_2,value_2,key_3,value_3,key_4,value_4,key_5,value_5 from tac where id=%d" % id
        db.execute(sql)

        res = db.fetchone()
        tac = Tac()
        if res:
            (id, name, key_1, value_1, 
                key_2, value_2, key_3, value_3, 
                key_4, value_4, key_5, value_5) = res

            tac.id = id
            tac.name = name

            for (key, value) in [
                    (key_1, value_1),
                    (key_2, value_2),
                    (key_3, value_3),
                    (key_4, value_4),
                    (key_5, value_5),]:
                key = key.strip()
                value = value.strip()
                if  key or value:
                    tac.map[key] = value
        return tac

    @staticmethod
    def from_db_by_func_tac_id(tac='taca_id', func_tac_id=-1):
        db = DB()
        sql = "select id,name,key_1,value_1,key_2,value_2,key_3,value_3,key_4,value_4,key_5,value_5 from tac where id=(select %s from func_tac_rel where id=%d)" % (tac, func_tac_id)
        db.execute(sql)

        res = db.fetchone()
        tac = Tac()

        if res:
            (id, name, 
                key_1, value_1,
                key_2, value_2,
                key_3, value_3,
                key_4, value_4,
                key_5, value_5,) = res

            tac = Tac( id = id, name = name)

            for (key, value) in [
                    (key_1, value_1),
                    (key_2, value_2),
                    (key_3, value_3),
                    (key_4, value_4),
                    (key_5, value_5),]:

                if key or value:
                    tac.map[key] = value
            return tac

    @staticmethod
    def del_func_tac_rel(func_tac_id):
        db = DB()
        db.execute("delete from func_tac_rel where id=%d" % func_tac_id)
        db.commit()

    def __nonzero__(self):
        return self.id != -1



if __name__ == '__main__':
    t = Tac()
    t.id = 1
    print bool(t)

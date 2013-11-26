# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 25, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
from webp.utils import strtpl
from webp.utils.db import DB

class AnchorStat(object):
    
    @staticmethod
    def search(tac_name, func_flag):
        db = DB()
        sql = strtpl("select a.id,c.name tac_name,d.name user_name,a.dt,a.status,a.description from func_tac_rel a,func b,tac c,user d where a.func_id=b.id and a.taca_id=c.id and a.user_id=d.id and b.flag=$func_flag and c.name like '%$tac_name%' order by a.dt desc").safe_substitute(dict(func_flag=func_flag, tac_name=tac_name))
        print 'sql', sql
        db.execute(sql)
        res = db.fetchall()
        _list = []
        for id, tac_name, user_name, dt, status, description in res:
            keys = dict(
                id = id,
                tac_name = tac_name,
                user_name = user_name,
                dt = dt,
                status = status, 
                description = description,
                )
            _list.append(keys)
        return _list








if __name__ == "__main__":
    pass


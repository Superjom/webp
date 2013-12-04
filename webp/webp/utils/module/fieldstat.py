# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 25, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
import sys
reload(sys);
# using exec to set the encoding, to avoid error in IDE.
exec("sys.setdefaultencoding('utf-8')");

from webp.utils import strtpl
from webp.utils.db import DB

class FieldStat(object):
    
    @staticmethod
    def search(tac_name, func_flag):
        print 'searching ...'
        db = DB()
        sql = strtpl("select a.id,c.name tac_name,d.name user_name,a.dt,a.status,a.description from func_tac_rel a,func b,tac c,user d where a.func_id=b.id and a.taca_id=c.id and a.user_id=d.id and b.flag='$func_flag' and c.name like '%$tac_name%' order by a.dt desc").safe_substitute(dict(func_flag=func_flag, tac_name=tac_name))
        print 'fieldstat search sql:', sql
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
                status_is_1 = (status == 1),
                status_is_m1 = (status == -1),
                status_is_0 = (status == 0))
            _list.append(keys)
        return _list








if __name__ == "__main__":
    pass



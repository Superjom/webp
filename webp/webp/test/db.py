# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 21, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
import MySQLdb

conn=MySQLdb.connect(host='10.48.56.63',user='root',passwd='123456',db='invlink',port=3306)
cur=conn.cursor()
cur.execute('select * from user')
cur.close()
conn.close()





if __name__ == "__main__":
    pass


# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 21, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
import MySQLdb

conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='invlink',port=3306)
cur=conn.cursor()

cur.execute(
    "select pwd,password('%s') mypwd from user where userid='%s'" % ('admin', 'admin'))

res = cur.fetchone()

print 'res', res

cur.close()
conn.close()





if __name__ == "__main__":
    pass


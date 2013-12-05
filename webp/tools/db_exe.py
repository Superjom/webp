# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 12 05, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
import sys
reload(sys);
# using exec to set the encoding, to avoid error in IDE.
exec("sys.setdefaultencoding('utf-8')");

import MySQLdb as mysql






if __name__ == "__main__":
    connection = mysql.connect(
        user="root",
        passwd="root",
        db="invlink",
        host="localhost",
        charset='utf8'
        )
    cursor = connection.cursor()

    sql = sys.argv[1]

    print "sql:\t", sql

    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()

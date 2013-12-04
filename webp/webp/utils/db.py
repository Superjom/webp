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

import MySQLdb as mysql
from webp.settings import DATABASES

default_db = DATABASES['default']

connection = mysql.connect(
    user=default_db['USER'],
    passwd=default_db['PASSWORD'],
    db=default_db['NAME'],
    host=default_db['HOST'],
    charset='utf8'
    )

class DB(object):
    def __init__(self):
        self.cursor = connection.cursor()
        # unity encode
        self.execute("SET NAMES utf8")

    def exe_commit(self, sql):
        self.execute(sql)
        self.commit()

    def execute(self, cmd):
        self.cursor.execute(cmd)

    def commit(self):
        #transaction.commit_unless_managed()
        connection.commit()

    def fetchone(self):
        res = self.cursor.fetchone()
        return res

    def fetchall(self):
        res = self.cursor.fetchall()
        return res

    def get_value(self, sql):
        self.execute(sql)
        res = self.fetchone()
        if res:
            return res[0]

    def __del__(self):
        self.cursor.close()


if __name__ == "__main__":
    db = DB()
    db.execute("select * from user")
    res = db.fetchone()
    print res


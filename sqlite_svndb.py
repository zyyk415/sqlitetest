#!/usr/bin/python
#coding=UTF-8

import sqlite3

conn =sqlite3.connect("F:\\00_SVN\\thd\\.svn\\wc.db")
#conn =sqlite3.connect("test.db")
cursor = conn.cursor()
print(cursor.execute("select * from sqlite_master"))
cursor.execute("select * from WORK_QUEUE")
print (cursor.fetchall())
#查找表WC_LOCK
cursor.execute("select * from WC_LOCK")
print (cursor.fetchall())
#cursor.execute("UPDATE Teachers SET Country='America' WHERE Id=1")
cursor.close()
conn.close()
#!/usr/bin/python3
"""accessing mysql database using MySQLdb"""
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="hbtn_0e_4_usa")
cur = db.cursor()
cur.execute("SELECT * FROM hbtn_0e_4_usa.states")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()

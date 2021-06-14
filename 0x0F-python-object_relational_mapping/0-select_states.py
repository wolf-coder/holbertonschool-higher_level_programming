#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
Your script should take 3 arguments:
mysql username, mysql password and database name
(no argument validation needed)
"""

import sys
import MySQLdb
username, password, database = sys.argv[1:]

db = MySQLdb.connect(host="localhost", user=username,
                     passwd=password, db=database)
cursor = db.cursor()
sql = "SELECT * FROM states"
cursor.execute(sql)
query_rows = cursor.fetchall()

for row in query_rows:
    print(row)

#!/usr/bin/python3
"""
Select from database with filter : names starting with N
"""

import sys
import MySQLdb


def Selector():
    """
    Select from database with filter : names starting with N
    """
    username, password, database = sys.argv[1:]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    sql = "select * from states WHERE name like \"N%\""
    cursor.execute(sql)
    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    Selector()

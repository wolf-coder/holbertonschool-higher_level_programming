#!/usr/bin/python3
"""
Select from database
"""

import sys
import MySQLdb


def Selector():
    """
    script that lists all states from the database hbtn_0_0_usa
    Your script should take 3 arguments:
    mysql username, mysql password and database name
    (no argument validation needed)
    """
    username, password, database = sys.argv[1:]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    sql = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(sql)
    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    Selector()

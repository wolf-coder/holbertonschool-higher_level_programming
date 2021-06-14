#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb


def Selector():
    """
    Write a script that takes in an argument and displays all
    values in the states table of hbtn_0e_0_usa where name matches
    the argument.
    """
    username, password, database, state = sys.argv[1:]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    sql = """
    SELECT * FROM states\
    WHERE name LIKE BINARY '{}'\
    ORDER BY id ASC
    """.format(state)

    cursor.execute(sql)
    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    Selector()

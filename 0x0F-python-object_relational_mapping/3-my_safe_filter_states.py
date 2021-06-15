#!/usr/bin/python3
"""
Preventing SQL Injection
"""

import sys
import MySQLdb


def Selector():
    """
    Selector with preventing SQL Injection
    """

    username, password, database, state = sys.argv[1:]
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database)

    with db.cursor() as cursor:
        cursor.execute("""
                       SELECT * FROM states
                       WHERE name LIKE  %(state)s """,
                       {'state': state}
                       )
        query_rows = cursor.fetchall()
        for row in query_rows:
            print(row)

    db.close()


if __name__ == "__main__":
    Selector()

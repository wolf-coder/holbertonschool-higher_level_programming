#!/usr/bin/python3
"""
Display cities table rows
"""

import sys
import MySQLdb


def Selector():
    """
    cities from the database hbtn_0e_4_usa
    """

    username, password, database, state = sys.argv[1:]
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database)

    with db.cursor() as cursor:
        cursor.execute("""
        SELECT cities.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %(state)s
        """, {'state': state}
                       )
        query_rows = cursor.fetchall()
        for idx in range(len(query_rows)):
            if idx == len(query_rows)-1:
                End = ''
            else:
                End = ', '
            print("{}".format(query_rows[idx][0]), end=End)
        print()
    db.close()


if __name__ == "__main__":
    Selector()

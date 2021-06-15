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

    username, password, database = sys.argv[1:]
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database)

    with db.cursor() as cursor:
        cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id;
        """
                       )
        query_rows = cursor.fetchall()
        for row in query_rows:
            print(row)

    db.close()


if __name__ == "__main__":
    Selector()

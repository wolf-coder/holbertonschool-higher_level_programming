#!/usr/bin/python3
"""
Write a script that adds the State object “Louisiana” to
the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import city


def Display_by_CitiesID(*kw):
    """
    Write a script that adds the State object “Louisiana” to
    the database hbtn_0e_6_usa
    """
    username, password, database = kw[0]

    """
    1) Connecting to DataBase
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)
    """

    2) Create Session
    """
    Session = sessionmaker()
    session = Session(bind=engine)

    """
    3)Display by Cities Ids
    """
    for c, s in session.query(city, State).filter(city.state_id ==
                                                  State.id).all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()


if __name__ == "__main__":
    Display_by_CitiesID(sys.argv[1:])

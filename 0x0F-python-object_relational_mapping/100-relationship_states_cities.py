#!/usr/bin/python3
"""
Write a script that adds the State object “Louisiana” to
the database hbtn_0e_6_usa
"""
import sys
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City


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
    newstate = State(name='California')
    newcity = City(name='San Francisco')
    newstate.cities.append(newcity)
    session.add(newstate)
    session.add(newcity)
    session.commit()


if __name__ == "__main__":
    Display_by_CitiesID(sys.argv[1:])
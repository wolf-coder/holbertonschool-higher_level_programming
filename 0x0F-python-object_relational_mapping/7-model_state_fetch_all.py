#!/usr/bin/python3
"""
Fetching table rows mode
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def Fetching(*kw):
    """
    Method to list all State objects from the database hbtn_0e_6_usa
    """

    """
    1) Connecting to DataBase
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(*kw[0]),
                           pool_pre_ping=True)

    """
    2) Create Session
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    3)Quering
    """
    for id, name in session.query(State.id, State.name):
        print("{}: {}".format(id, name))


if __name__ == "__main__":
    Fetching(sys.argv[1:])

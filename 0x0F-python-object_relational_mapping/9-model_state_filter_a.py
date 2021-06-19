#!/usr/bin/python3
"""
Write a script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def Fetching(*kw):

    """
    Method to Write list all State objects that contain the
    letter a from the database hbtn_0e_6_usa
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

    for instance in session.query(State).filter(State.name.like('%a%')):
        print("{}: {}".format(instance.id, instance.name))


if __name__ == "__main__":
    Fetching(sys.argv[1:])

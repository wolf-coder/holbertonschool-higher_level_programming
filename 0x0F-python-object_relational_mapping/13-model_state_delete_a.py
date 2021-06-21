#!/usr/bin/python3
"""
Write a script that adds the State object “Louisiana” to
the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def Deleting(*kw):

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
    3)deleting if name contains character `a`
    """
    for row in session.query(State).filter(State.name.like('%a%')):
        session.delete(row)
    session.commit()
    session.close()


if __name__ == "__main__":
    Deleting(sys.argv[1:])

#!/usr/bin/python3
"""
Write a script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def Fetching(*kw):

    """
    Write a script that prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa.
    """

    """
    1) Connecting to DataBase
    """
    *login, searched = *kw[0],
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(*login),
                           pool_pre_ping=True)
    """
    2) Create Session
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    3)Quering
    """
    Demanded_state = session.query(State).filter_by(name=searched).first()
    if Demanded_state:
        print("{}".format(Demanded_state.id))
    else:
        print("Not found")


if __name__ == "__main__":
    Fetching(sys.argv[1:])

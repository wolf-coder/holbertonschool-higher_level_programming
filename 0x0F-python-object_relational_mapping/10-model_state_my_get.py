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
    username, password, database, searched = kw[0]

    """
    1) Connecting to DataBase
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)
    """
    2) Create Session
    """
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    """
    3)Quering
    """
    Demanded_state = session.query(State).filter_by(name=searched).first()
    if Demanded_state:
        print("{}".format(Demanded_state.id))
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    Fetching(sys.argv[1:])

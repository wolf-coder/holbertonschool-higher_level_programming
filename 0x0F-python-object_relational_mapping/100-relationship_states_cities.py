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


def Display_by_CitiesID():
    """
    Write a script that adds the State object “Louisiana” to
    the database hbtn_0e_6_usa
    """
    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost/{}'
                            .format(
                                        sys.argv[1],
                                        sys.argv[2],
                                        sys.argv[3]
                                            ),
                            pool_pre_ping=True
                                )
    """
    2) Create Session
    """
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    """
    3)Display by Cities Ids
    """
    new_State = State(name="California")
    new_State.cities = [City(name="San Francisco")]
    Rel = session.add(new_State)
    session.commit()
    session.close()


if __name__ == "__main__":
    Display_by_CitiesID()

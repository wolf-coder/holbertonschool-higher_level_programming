#!/usr/bin/python3
"""
Class definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from model_state import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    Defining mapped classes
    """

    __tablename__ = 'cities'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'))

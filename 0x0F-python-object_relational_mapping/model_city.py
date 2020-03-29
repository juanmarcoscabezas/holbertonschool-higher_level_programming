#!/usr/bin/python3
"""
This module contains the City class definition
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """
    State is a mapped class of the city table

    Attributes:
        __tablename__: SQL table name
        id: id field
        name: name field
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

#!/usr/bin/python3
"""
This module contains the State class definition
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    State is a mapped class of the state table

    Attributes:
        __tablename__: SQL table name
        id: id field
        name: name field
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

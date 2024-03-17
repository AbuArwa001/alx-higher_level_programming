#!/usr/bin/python3
""" Module that contains the class definition of
a State and an instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String, Sequence , ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
        Class for mapping States to states in Mysql DB
    """
    __tablename__ = 'cities'
    id = Column(Integer, Sequence('states_id_seq'), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),  nullable=False)


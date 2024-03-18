#!/usr/bin/python3
""" Module that contains the class definition of
a State and an instance Base = declarative_base()"""
# relationship_state.py
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class for mapping states to State in Mysql DB
    """
    __tablename__ = 'states'
    id = Column(Integer, Sequence('states_id_seq'), primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade="all, delete, delete-orphan")

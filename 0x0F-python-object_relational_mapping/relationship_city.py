#!/usr/bin/python3
""" Module that contains the class definition of
a State and an instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
    Class for mapping cities to City in Mysql DB
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    # state = relationship("State", back_populates="cities")

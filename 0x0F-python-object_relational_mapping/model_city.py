#!/usr/bin/python3
"""model_city defines the City class"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base
from model_state import State


class City(Base):
    """City class
    objects are mapped to MySQL rows in the cities table
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))

    state = relationship('State', back_populates="cities")

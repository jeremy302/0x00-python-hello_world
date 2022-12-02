#!/usr/bin/python3
''' <TODO> docstring of the module for the relevant question '''
from sqlalchemy import Column, ForeignKey, Integer, String

from relationship_state import Base


class City(Base):
    ''' class for a state's city '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

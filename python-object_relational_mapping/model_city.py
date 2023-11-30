#!/usr/bin/python3
"""First state model"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    """class City"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)

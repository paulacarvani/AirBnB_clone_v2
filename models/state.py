#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from models.base_model import BaseModel, Base
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if models.type_storage == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City')
    else:
        name = ''
        cities = models.storage.all(City)

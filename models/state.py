#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from models.base_model import BaseModel, Base
import models
from models.city import City


if getenv("HBNB_TYPE_STORAGE") == "db":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City')
else:
    class State(BaseModel):
        """ Defined class to work with FileStorage'"""
        name = ''

        @property
        def cities(self):
            """return values"""
            cities = models.storage.all(City).values()
            lis_values = []
            for i in cities:
                if i.state_id == self.id:
                    lis_values.append(i)
            return lis_values

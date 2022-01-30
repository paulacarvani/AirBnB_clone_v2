#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


if models.type_storage == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='states')

else:
    class State(BaseModel):
        """ State class """
        name = ""

        @property
        def cities(self):
            """Return the list of cities linked to State"""
            city_list = []
            all_cities = models.storage.all(City)

            for c in all_cities.values():
                if c.state_id == self.id:
                    city_list.append(c)
            return city_list

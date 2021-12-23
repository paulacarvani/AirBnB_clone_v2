#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models
from models.city import City
from os import getenv
import sqlalchemy

if getenv('HBNB_type_storage') == "db":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        name = Column(String(128), nullable==False)
        cities = relationship('City', backref='state')

else:
    class State(BaseModel):
        name = ""

        @property
        def cities(self):
            cities_List = []
            for cities in models.storage.all(City).values():
                if cities.places_id ==self.id:
                    cities_List.append(cities)
            return cities_List

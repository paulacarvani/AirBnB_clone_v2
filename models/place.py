#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
import models
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import String, Integer, Float

from os import getenv
from models.review import Review
from models.amenity import Amenity


column_amenity = Column('amenity_id', String(60), ForeignKey('amenities.id'),
                        nullable=False)
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             nullable=False),
                      column_amenity)

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class Place(BaseModel, Base):
        """ A place to stay """
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship('Amenity', secondary='place_amenity',
                                 back_populates='place_amenities',
                                 viewonly=False)

else:
    class Place(BaseModel):
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = ''
        number_bathrooms = ''
        max_guest = ''
        price_by_night = ''
        latitude = ''
        longitude = ''
        amenity_ids = []

        @property
        def reviews(self):
            """
            returns the list of Review instances with place_id equals
            to the current Place.id => It will be the FileStorage
            relationship between Place and Review
            """
            total_reviews = models.storage.all(Review)
            result = []
            for each in total_reviews.values():
                result.append(each)
            return result

        @property
        def amenities(self):
            """Getter to amenities"""
            self.amenity_ids = models.storage.all(Amenity)
            return self.amenity_ids

        @amenities.setter
        def amenities(self, id):
            """ Function setter to amenities """
            if id.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(id)

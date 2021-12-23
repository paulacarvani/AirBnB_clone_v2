#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import models


class Amenity(BaseModel, Base):
    if models.type_storage == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        # place_amenities = relationship("Place")
    else:
        name = ""

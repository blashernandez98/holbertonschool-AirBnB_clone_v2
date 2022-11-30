#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if (getenv('HBNB_TYPE_STORAGE') != 'db'):
        @property
        def cities(self):
            from models import storage
            from models.city import City
            list_city = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city

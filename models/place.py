#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity_table = Table(
        'place_amenity', Base.metadata,
        Column(
            'place_id', String(60), ForeignKey('places.id'),
            primary_key=True, nullable=False),
        Column(
            'amenity_id', String(60), ForeignKey('amenities.id'),
            primary_key=True, nullable=False))


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
    amenity_ids = []

    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        reviews = relationship(
            'Review', cascade='all, delete', backref='place')
        amenities = relationship(
            'Amenity', secondary='place_amenity',
            viewonly=False)
    else:
        @property
        def reviews(self):
            list_rev = []
            from models import storage
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    list_rev.append(review)
            return list_rev

        @property
        def amenities(self):
            list_ame = []
            from models import storage
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    list_ame.append(amenity)
            return list_ame

        @amenities.setter
        def amenities(self, ame):
            if 'Amenity' not in type(ame):
                return
            self.amenity_ids.append(ame.id)

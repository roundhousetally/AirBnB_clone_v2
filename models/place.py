#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    metadata = Base.metadata
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', cascade="all, delete", backref="place")
    place_amenity = Table("place_amenity", metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False, backref="places")
    amenity_ids = []

    @property
    def reviews(self):
        """ returns list of Reviews """
        from models.engine import FileStorage
        l = []
        for k, v in FileStorage.__objects.items():
            if v.place_id == self.id:
                l.append(v)
        return l

    @property
    def amenities(self):
        """ returns list of Reviews """
        from models.engine import FileStorage
        l = []
        for k, v in FileStorage.__objects.items():
            if v.amenity_ids == self.id:
                l.append(v)
        return l

    @amenities.setter
    def amenities(self, amenobj):
        """ handles append method """
        from models.amenity import Amenity
        if type(amenobj) is not Amenity:
            return
        else:
            amenity_ids.append(amenobj.id)

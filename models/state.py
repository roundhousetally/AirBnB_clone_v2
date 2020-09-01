#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import environ
import models

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="all, delete", backref='state')



    if environ.get("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            ''' getter for FileStorage cities-state '''
            l = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    l.append(city)
                    return l

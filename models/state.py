#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="all, delete", backref='state')

    @property
    def cities(self):
        ''' getter for FileStorage cities-state '''
        from models.engine import FileStorage
        l = []
        for k, v in FileStorage.__objects.items():
            if v.state_id == self.id:
                l.append(v)
        return l

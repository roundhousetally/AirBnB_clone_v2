#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        """ initialize up in this bitch """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}".
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        conn = self.__engine.connect()
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """ reload up in this m'fer """
        Base.metadata.create_all(self.__engine)
        SessMaker = sessionmaker(bind=self.__engine,
                                 expire_on_commit=False)
        self.__session = scoped_session(SessMaker)

    def all(self, cls=None):
        ''' alllllllllllllllll '''
        if cls is None:
            qry = self.__session.query(User, State, City,
                                       Amenity, Place, Review)
        else:
            qry = self.__session.query(cls)
        ret_dict = dict()
        for rec in qry:
            print("REC BITCH REC")
            print(type(rec))
            print(rec)
#           k = cls.__name__ + "." rec.id
#           ret_dict[k] = rec
        return ret_dict

    def new(self, obj):
        ''' newwwwwwwwwwwwwwwwwwww '''
        if obj is None:
            return
        self.__session.add(obj)

    def save(self):
        ''' help, save me, I'm drowning. someone call the ghostbusters! '''
        self.__session.commit()

    def delete(self, obj=None):
        """ NONE. NONE AT ALL """
        if obj is None:
            return
        else:
            self.__session.delete(obj)

#!/usr#!/usrython3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine
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
#       conn = self.__engine.connect()
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """ reload up in this m'fer """
        from sqlalchemy.orm import sessionmaker, scoped_session
        Base.metadata.create_all(self.__engine)
        SessMaker = sessionmaker(bind=self.__engine,
                                 expire_on_commit=False)
        Session = scoped_session(SessMaker)
        self.__session = Session()
#       print("save yourself... db 41")
#       print(self.__session)

    def all(self, cls=None):
        ''' alllllllllllllllll '''
#       print("db 46")
#       print(type(cls))
#       print(cls)
#       print(self.__session)
        qry = []
        if cls is None:
            qry += self.__session.query(State)
            qry += self.__session.query(City)
            qry += self.__session.query(Amenity)
            qry += self.__session.query(Review)
            qry += self.__session.query(Place)
            qry += self.__session.query(User)
        else:
            qry = self.__session.query(cls)
        ret_dict = dict()
#       print(qry)
#       print("lllllllllllllllllllllllllllllllllllllllll db 53")
        for rec in qry:
            k = rec.__class__.__name__ + "." + rec.id
            ret_dict[k] = rec
#       print("DB 69 B4 RETURN PPAP")
#       print(ret_dict)
        return ret_dict

    def new(self, obj):
        ''' newwwwwwwwwwwwwwwwwwww '''
        if obj is None:
            return
        self.__session.add(obj)

    def save(self):
        ''' help, save me, I'm drowning. someone call the ghostbusters! '''
#       print("SAVE ME SAVE ME db 70")
#       print(self.__session)
        self.__session.commit()
#       print("COMMITTED db 73")

    def delete(self, obj=None):
        """ NONE. NONE AT ALL """
        if obj is None:
            return
        else:
            self.__session.delete(obj)

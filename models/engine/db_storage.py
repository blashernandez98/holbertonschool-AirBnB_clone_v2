#!/usr/bin/python3
""" Module for db storage engine """
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker, Session
import os


classes = {'User': User, 'Place': Place, 'Amenity': Amenity,
            'State': State, 'City': City, 'Review': Review}


class DBStorage:
    """ Database storage class """
    __engine = None
    __session = None

    def __init__(self):
        """ Custom init method """
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        mode = os.getenv('HBNB_ENV')

        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{database}",
            pool_pre_ping=True)

        if mode == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns objects stored in db """
        obj_dic = {}

        if cls:
            for row in self.__session.query(cls).all():
                obj_dic[f"{type(row).__name__}.{row.id}"] = row
        else:
            for model in classes.values():
                for row in self.__session.query(model):
                    obj_dic[f"{type(row).__name__}.{row.id}"] = row
        return obj_dic

    def new(self, obj):
        """ Adds object to session """
        if obj is None:
            return
        self.__session.add(obj)

    def save(self):
        """ Commits current changes in session """
        self.__session.commit()

    def reload(self):
        """ Reloads """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False)
        self.__session = scoped_session(session)

#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime ,nullable=False, default=datetime.utcnow())
    updated_at= Column(DateTime ,nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            from models import storage
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            for myKey, myValue in kwargs.items():
                if myKey == 'updated_at' or myKey == 'created_at':
                    myValue = datetime.strptime(kwargs[myKey],
                                            '%Y-%m-%dT%H:%M:%S.%f')
                if myKey != '__class__':
                    setattr(self, myKey, myValue)
            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = datetime.now()
                setattr(self, "updated_at", kwargs['updated_at'])
            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.now()
                setattr(self, "created_at", kwargs['created_at'])

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """A method to delete an element from the storage"""
        from models import storage
        storage.delete(self)

# hbnb_dev_pwd``
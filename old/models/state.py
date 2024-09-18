#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from models.city import City
from sqlalchemy import String
from sqlalchemy.orm import relationship
from os import getenv
import models

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")
    
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            theReturnedList = []
            for myCity in list(models.storage.all(City).values()):
                if myCity.state_id == self.id:
                    theReturnedList.append(myCity)
            return theReturnedList

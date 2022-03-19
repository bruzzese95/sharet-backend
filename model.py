from click import DateTime
from pydantic import BaseModel
from typing import List
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.orm import relationship


base = declarative_base()


class User(base):
    __tablename__ = "user"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String)

   
class SharedResource(base):
    __tablename__ = "resource"

    id = Column(Integer, Sequence("resource_id_seq"), primary_key=True, unique=True)
    name = Column(String)
    owner = Column(Integer)
    users = Column(Integer)
    


class Reservation(base):
    __tablename__ = "reservation"

    idReservation = Column(Integer, Sequence("reservation_id_seq"), primary_key=True, unique=True)
    idResource = Column(Integer)
    owner = Column(Integer)
    datetime = Column(Integer)
    timelenght = Column(Integer)


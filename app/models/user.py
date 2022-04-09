from collections import UserList
from pydantic import EmailStr
from sqlalchemy import ForeignKey, Integer, String, Column, ARRAY
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    idToken = Column(String, primary_key=True, index=True)
    idUser = Column(Integer, nullable=False, index=True)
    name = Column(String, nullable=False)
    email = Column(String, index=True, nullable=False)
    
    reservations = relationship(
        "Reservation",
        cascade="all,delete-orphan",
        back_populates="owner",
        uselist=True
    )

    userandresource = relationship(
        "User_And_Resource",
        cascade="all,delete-orphan",
        back_populates="user",
        uselist=True
    )
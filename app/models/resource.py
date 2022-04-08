from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Resource(Base):
    id = Column(Integer, primary_key=True, unique=False)
    name = Column(String)

    reservations = relationship(
        "Reservation",
        cascade="all,delete-orphan",
        back_populates="resource",
        uselist=True
    )

    userandresource = relationship(
        "User_And_Resource",
        cascade="all,delete-orphan",
        back_populates="resource",
        uselist=True
    )
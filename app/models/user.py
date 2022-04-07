from pydantic import EmailStr
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    idToken = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, index=True, nullable=False)
    
    
    resources = relationship(
        "Resource",
        cascade="all,delete-orphan",
        back_populates="owner",
        uselist=True,
    )
    
    reservations = relationship(
        "Reservation",
        cascade="all,delete-orphan",
        back_populates="owner",
        uselist=True
    )
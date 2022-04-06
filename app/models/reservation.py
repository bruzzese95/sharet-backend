from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Reservation(Base):
    id = Column(Integer, primary_key=True, index=True)
    idResource = Column(Integer, ForeignKey("resource.id"), nullable=False)
    idOwner = Column(String, ForeignKey("user.idToken"), nullable=False)
    name = Column(String, nullable=False)
    startTime = Column(String, nullable=False)
    endTime = Column(String, nullable=False)

    resource = relationship("Resource", back_populates="reservations")
    owner = relationship("User", back_populates="reservations")
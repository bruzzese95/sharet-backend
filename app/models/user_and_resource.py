from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User_And_Resource(Base):
    id = Column(Integer, primary_key=True, index=True)
    idUser = Column(String, ForeignKey("user.idToken"), nullable=False)    
    idResource = Column(Integer,ForeignKey("resource.id"), nullable=False)

    user = relationship("User", back_populates="userandresource")
    resource = relationship("Resource", back_populates="userandresource")
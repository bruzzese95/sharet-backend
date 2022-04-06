from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Resource(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)    
    owner_id = Column(String,ForeignKey("user.idToken"), nullable=False)
    owner = relationship("User", back_populates="resources")
    
    '''users = Column(String(256), nullable=True)'''
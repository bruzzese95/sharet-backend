from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()

class User(base):
    __tablename__= "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(256), nullable=True)
    surname = Column(String(256), nullable=True)
    email = Column(String, index=True, nullable=False)
    resources = relationship(
        "Resource",
        cascade="all,delete-orphan",
        back_populates="owner",
        uselist=True,
    )

class Resource(base):
    __tablename__ = "resource"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    owner_id = Column(Integer, nullable=False)
    owner = relationship("User", back_populates="resources")
    
    '''users = Column(String(256), nullable=True)'''
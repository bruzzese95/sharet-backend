from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    idToken = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    '''first_name = Column(String(256), nullable=False)
    surname = Column(String(256), nullable=True)
    email = Column(String, index=True, nullable=True)'''
    
    
    resources = relationship(
        "Resource",
        cascade="all,delete-orphan",
        back_populates="owner",
        uselist=True,
    )
    
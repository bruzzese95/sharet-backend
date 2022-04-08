from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    idToken: str
    name: str
    email: str
    shared_resources: Optional[list[int]]


# Properties to receive via API on creation
class UserCreate(UserBase):
    idToken: str
    name: str
    email: str
    shared_resources: Optional[list[int]]


# Properties to receive via API on update
class UserUpdate(UserBase):
    idToken: str
    name: Optional[str]
    email: Optional[str]
    shared_resources: Optional[list[int]]


class UserInDBBase(UserBase):
    idToken: str
    name: str
    email: str
    shared_resources: Optional[list[int]]

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass

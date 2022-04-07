from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    idToken: str
    name: str
    email: str


# Properties to receive via API on creation
class UserCreate(UserBase):
    ...


# Properties to receive via API on update
class UserUpdate(UserBase):
    ...


class UserInDBBase(UserBase):
    idToken: Optional[str]

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass

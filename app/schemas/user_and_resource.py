from pydantic import BaseModel

from typing import Sequence


class UserAndResourceBase(BaseModel):
    id: int
    idUser: str
    idResource: int


class UserAndResourceCreate(UserAndResourceBase):
    id: int
    idUser: str
    idResource: int


class UserAndResourceUpdate(UserAndResourceBase):
    id: int
    idUser: str
    idResource: int


# Properties shared by models stored in DB
class UserAndResourceInDBBase(UserAndResourceBase):
    id: int
    idUser: str
    idResource: int

    class Config:
        orm_mode = True


# Properties to return to client
class UserAndResource(UserAndResourceInDBBase):
    pass


# Properties properties stored in DB
class UserAndResourceInDB(UserAndResourceInDBBase):
    pass


class UserAndResourceSearchResults(BaseModel):
    userAndResourceDtoList: Sequence[UserAndResource]

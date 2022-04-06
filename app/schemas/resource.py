from pydantic import BaseModel

from typing import Sequence


class ResourceBase(BaseModel):
    id: int
    name: str
    owner_id: str


class ResourceCreate(ResourceBase):
    id: int
    name: str
    owner_id: str


class ResourceUpdate(ResourceBase):
    name: str


# Properties shared by models stored in DB
class ResourceInDBBase(ResourceBase):
    id: int
    name: str
    owner_id: str

    class Config:
        orm_mode = True


# Properties to return to client
class Resource(ResourceInDBBase):
    pass


# Properties properties stored in DB
class ResourceInDB(ResourceInDBBase):
    pass


class ResourceSearchResults(BaseModel):
    sharedResourceDtoList: Sequence[Resource]

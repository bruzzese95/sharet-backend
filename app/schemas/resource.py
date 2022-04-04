from pydantic import BaseModel

from typing import Sequence


class ResourceBase(BaseModel):
    name: str
    owner_id: int


class ResourceCreate(ResourceBase):
    name: str
    owner_id: int


class ResourceUpdate(ResourceBase):
    name: str


# Properties shared by models stored in DB
class ResourceInDBBase(ResourceBase):
    id: int
    owner_id: int

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

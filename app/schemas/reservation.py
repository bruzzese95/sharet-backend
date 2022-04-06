from pydantic import BaseModel

from typing import Sequence


class ReservationBase(BaseModel):
    id: int
    idResource: int
    idOwner: str
    name: str
    startTime: str
    endTime: str


class ReservationCreate(ReservationBase):
    id: int
    idResource: int
    idOwner: str
    name: str
    startTime: str
    endTime: str


class ReservationUpdate(ReservationBase):
    name: str


# Properties shared by models stored in DB
class ReservationInDBBase(ReservationBase):
    id: int
    idResource: int
    idOwner: str
    name: str
    startTime: str
    endTime: str

    class Config:
        orm_mode = True


# Properties to return to client
class Reservation(ReservationInDBBase):
    pass


# Properties properties stored in DB
class ReservationInDB(ReservationInDBBase):
    pass


class ReservationSearchResults(BaseModel):
    sharedResourceDtoList: Sequence[Reservation]

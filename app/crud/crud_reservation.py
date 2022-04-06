from app.crud.base import CRUDBase
from app.models.reservation import Reservation
from app.schemas.reservation import ReservationCreate, ReservationUpdate


class CRUDReservation(CRUDBase[Reservation, ReservationCreate, ReservationUpdate]):
    ...


reservation = CRUDReservation(Reservation)



'''
TO DO implement Reservation table

class Reservation(base):
    __tablename__ = "reservation"

    idReservation = Column(Integer, Sequence("reservation_id_seq"), primary_key=True, unique=True)
    idResource = Column(Integer)
    owner = Column(Integer)
    datetime = Column(Integer)
    timelenght = Column(Integer)

    '''
from sqlalchemy import Column, Integer, String, Date
from database import Base

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    room_number = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String, default="Confirmed")
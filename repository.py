from sqlalchemy.orm import Session
from models import Booking

class BookingRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, booking: Booking) -> Booking:
        self.db.add(booking)
        self.db.commit()
        self.db.refresh(booking)
        return booking
    
    def get_all(self) -> list[Booking]:
        return self.db.query(Booking).all()
    
    def get_by_id(self, booking_id: int) -> Booking | None:
        return self.db.query(Booking).filter(Booking.id == booking_id).first()
    
    def update(self, booking_id: int, booking: Booking) -> Booking:
       existing_booking = self.get_by_id(booking_id)
       if not existing_booking:
           raise ValueError("Booking not found")
       existing_booking.customer_name = booking.customer_name
       existing_booking.room_number = booking.room_number
       existing_booking.date = booking.date
       existing_booking.status = booking.status

       self.db.commit()
       self.db.refresh(existing_booking)
       return existing_booking
    
    def delete(self, booking_id: int) -> None:
        booking = self.get_by_id(booking_id)
        if not booking:
            raise ValueError("Booking not found")
        self.db.delete(booking)
        self.db.commit()
    
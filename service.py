from sqlalchemy.orm import Session
from models import Booking
from schemas import BookingCreate, BookingUpdate
from repository import BookingRepository

class BookingService:
    def __init__(self, db: Session):
        self.repository = BookingRepository(db)
    
    def create_booking(self, data: BookingCreate) -> Booking:
        new_booking = Booking(
        customer_name = data.customer_name,
        room_number=data.room_number,
        date=data.date
        )
        return self.repository.create(new_booking)
    
    def get_all_bookings(self) -> list[Booking]:
        return self.repository.get_all()
    
    def get_booking(self, booking_id) -> Booking:
        booking = self.repository.get_by_id(booking_id)
        if not booking:
            raise ValueError("Booking not found")
        return booking
    
    def update_booking(self, booking_id: int, data: BookingUpdate) -> Booking:
        updated_booking = Booking(
        customer_name = data.customer_name,
        room_number=data.room_number,
        date=data.date,
        status=data.status
        )
        return self.repository.update(booking_id, updated_booking)
    
    def delete_booking(self, booking_id: int) -> None:
        return self.repository.delete(booking_id)
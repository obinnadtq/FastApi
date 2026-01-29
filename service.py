from models import Booking
from schemas import BookingCreate
from repository import BookingRepository

class BookingService:
    def __init__(self, repository: BookingRepository):
        self.repository = repository
        self._id_counter = 1
    
    def create_booking(self, data: BookingCreate) -> Booking:
        new_booking = Booking(
        id=self._id_counter,
        customer_name = data.customer_name,
        room_number=data.room_number,
        date=data.date
        )
        self._id_counter += 1
        return self.repository.create(new_booking)
    
    def get_all_bookings(self) -> list[Booking]:
        return self.repository.get_all()
    
    def get_booking(self, booking_id) -> Booking:
        booking = self.repository.get_by_id(booking_id)
        if not booking:
            raise ValueError("Booking not found")
        return booking
    
    def update_booking(self, booking_id: int, data: BookingCreate) -> Booking:
        booking = self.get_booking(booking_id)
        updated_booking = Booking(
        id=booking.id,
        customer_name = data.customer_name,
        room_number=data.room_number,
        date=data.date,
        status=booking.status
        )
        return self.repository.update(booking_id, updated_booking)
    
    def delete_booking(self, booking_id: int) -> None:
        booking = self.get_booking(booking_id)
        return self.repository.delete(booking.id)
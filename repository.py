from models import Booking

class BookingRepository:
    def __init__(self):
        self._bookings: list[Booking] = []

    def create(self, booking: Booking) -> Booking:
        self._bookings.append(booking)
        return booking
    
    def get_all(self) -> list[Booking]:
        return self._bookings
    
    def get_by_id(self, booking_id: int) -> Booking | None:
        return next((b for b in self._bookings if b.id == booking_id), None)
    
    def update(self, booking_id: int, booking: Booking) -> Booking:
        for index, existing in enumerate(self._bookings):
            if existing.id == booking_id:
                self._bookings[index] = booking
                return booking
        raise ValueError("Booking not found")
    
    def delete(self, booking_id: int) -> None:
        self._bookings = [ b for b in self._bookings if b.id != booking_id]

    
from dataclasses import dataclass
from datetime import date

@dataclass
class Booking:
    id: int
    customer_name: str
    room_number: int
    date: date
    status: str = "confirmed"
from pydantic import BaseModel
from datetime import date

class BookingCreate(BaseModel):
    customer_name: str
    room_number: int
    date: date

class BookingResponse(BaseModel):
    id: int
    customer_name: str
    room_number: int
    date: date
    status: str
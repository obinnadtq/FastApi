from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date

app = FastAPI(title="Simple Booking System")

class Booking(BaseModel):
    id: int
    customer_name: str
    room_number: int
    date: date
    status: str = "confirmed"

class BookingCreate(BaseModel):
    customer_name: str
    room_number: int
    date: date

bookings: list[Booking] =[]

@app.post("/bookings", response_model=Booking)
def create_booking(booking: BookingCreate):
    new_booking = Booking(
        id=len(bookings) + 1,
        customer_name = booking.customer_name,
        room_number=booking.room_number,
        date=booking.date,
        status="confirmed"
    )
    bookings.append(new_booking)
    return new_booking

@app.get("/bookings", response_model=list[Booking])
def get_bookings():
    return bookings

@app.get("/bookings/{id}", response_model=Booking)
def get_booking(id: int):
    for booking in bookings:
        if booking.id == id:
            return booking
    raise HTTPException(status_code = 404, detail= "Booking not found")

@app.put("/bookings/{id}", response_model=Booking)
def update_booking(id: int, updated: BookingCreate):
    for index, booking in enumerate(bookings):
        if booking.id == id:
            bookings[index] = Booking(
        id=id,
        customer_name = updated.customer_name,
        room_number=updated.room_number,
        date=updated.date,
        status=booking.status
        )
        return bookings[index]
    raise HTTPException(status_code = 404, detail= "Booking not found")

@app.delete("/bookings/{id}")
def delete_booking(id: int):
    for index, booking in enumerate(bookings):
        if booking.id == id:
            bookings.pop(index)
            return {"message": "Booking deleted"}
    raise HTTPException(status_code = 404, detail= "Booking not found")
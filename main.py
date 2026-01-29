from fastapi import FastAPI, HTTPException
from schemas import BookingCreate, BookingResponse
from repository import BookingRepository
from service import BookingService

app = FastAPI(title="Booking System")

repository = BookingRepository()
service = BookingService(repository)


@app.post("/bookings", response_model=BookingResponse)
def create_booking(booking: BookingCreate):
    return service.create_booking(booking)
    

@app.get("/bookings", response_model=list[BookingResponse])
def get_bookings():
    return service.get_all_bookings()

@app.get("/bookings/{id}", response_model=BookingResponse)
def get_booking(id: int):
    try:
        return service.get_booking(id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Booking not found")

@app.put("/bookings/{id}", response_model=BookingResponse)
def update_booking(id: int, updated: BookingCreate):
    try:
        return service.update_booking(id, updated)
    except ValueError:
        raise HTTPException(status_code=404, detail="Booking not found")
    
@app.delete("/bookings/{id}")
def delete_booking(id: int):
    try:
        service.delete_booking(id)
        return {"message": "Booking deleted"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Booking not found")
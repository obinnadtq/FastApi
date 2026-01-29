from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import BookingCreate, BookingResponse, BookingUpdate
from service import BookingService
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Booking System")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/bookings", response_model=BookingResponse)
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    service = BookingService(db)
    return service.create_booking(booking)
    

@app.get("/bookings", response_model=list[BookingResponse])
def get_bookings(db: Session = Depends(get_db)):
    service = BookingService(db)
    return service.get_all_bookings()

@app.get("/bookings/{id}", response_model=BookingResponse)
def get_booking(id: int, db: Session = Depends(get_db)):
    service = BookingService(db)
    try:
        return service.get_booking(id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Booking not found")

@app.put("/bookings/{id}", response_model=BookingResponse)
def update_booking(id: int, updated: BookingUpdate, db: Session = Depends(get_db)):
    service = BookingService(db)
    try:
        return service.update_booking(id, updated)
    except ValueError:
        raise HTTPException(status_code=404, detail="Booking not found")
    
@app.delete("/bookings/{id}")
def delete_booking(id: int, db: Session = Depends(get_db)):
    service = BookingService(db)
    try:
        service.delete_booking(id)
        return {"message": "Booking deleted"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Booking not found")
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Base
import logging

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Backend_Api_For_Hotel1,_Providing_A_Scalable_And_Secure_Infrastructure_For_Managing_Hotel_Operations,_Including_Room_Bookings,_Customer_Management,_And_Staff_Administration. API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API is running", "endpoints": 15}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/users")
def users(db: Session = Depends(get_db)):
    return {"message": "Endpoint /users", "method": "GET"}

@app.post("/users")
def users(data: dict, db: Session = Depends(get_db)):
    return {"message": "Created", "data": data}

@app.get("/users/{id}")
def users_id(db: Session = Depends(get_db)):
    return {"message": "Endpoint /users/{id}", "method": "GET"}

@app.put("/users/{id}")
def users_id(data: dict, db: Session = Depends(get_db)):
    return {"message": "Updated", "data": data}

@app.delete("/users/{id}")
def users_id(db: Session = Depends(get_db)):
    return {"message": "Deleted"}

@app.get("/hotels")
def hotels(db: Session = Depends(get_db)):
    return {"message": "Endpoint /hotels", "method": "GET"}

@app.post("/hotels")
def hotels(data: dict, db: Session = Depends(get_db)):
    return {"message": "Created", "data": data}

@app.get("/hotels/{id}")
def hotels_id(db: Session = Depends(get_db)):
    return {"message": "Endpoint /hotels/{id}", "method": "GET"}

@app.put("/hotels/{id}")
def hotels_id(data: dict, db: Session = Depends(get_db)):
    return {"message": "Updated", "data": data}

@app.delete("/hotels/{id}")
def hotels_id(db: Session = Depends(get_db)):
    return {"message": "Deleted"}

@app.get("/bookings")
def bookings(db: Session = Depends(get_db)):
    return {"message": "Endpoint /bookings", "method": "GET"}

@app.post("/bookings")
def bookings(data: dict, db: Session = Depends(get_db)):
    return {"message": "Created", "data": data}

@app.get("/bookings/{id}")
def bookings_id(db: Session = Depends(get_db)):
    return {"message": "Endpoint /bookings/{id}", "method": "GET"}

@app.put("/bookings/{id}")
def bookings_id(data: dict, db: Session = Depends(get_db)):
    return {"message": "Updated", "data": data}

@app.delete("/bookings/{id}")
def bookings_id(db: Session = Depends(get_db)):
    return {"message": "Deleted"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

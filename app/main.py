from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.routes import user,flight
app = FastAPI(title="Flight Ticket Booking Agent")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def health_check():
    return {"status": "Agent is running"}

@app.post("/preferences/")
def create_preference(
    preference: schemas.TicketPreferenceCreate,
    db: Session = Depends(get_db)
):
    db_pref = models.TicketPreference(**preference.dict())
    db.add(db_pref)
    db.commit()
    db.refresh(db_pref)
    return db_pref

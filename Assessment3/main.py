import os
import sys
import shutil
from typing import List


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

import models
import schemas
from db import engine, get_db

models.Base.metadata.create_all(bind=engine)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI(title="Event RSVP System")


app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")


# ── POST /events/ 
@app.post("/events/", response_model=schemas.EventOut, status_code=201)
async def create_event(
    title: str = Form(...),
    description: str = Form(...),
    date: str = Form(...),
    location: str = Form(...),
    flyer: UploadFile = File(None),
    db: Session = Depends(get_db),
):
    """Create a new event, optionally with a flyer image."""
    flyer_filename = None

    if flyer and flyer.filename:
  
        safe_filename = f"{flyer.filename}"
        file_path = os.path.join(UPLOAD_DIR, safe_filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(flyer.file, buffer)
        flyer_filename = safe_filename

    new_event = models.Event(
        title=title,
        description=description,
        date=date,
        location=location,
        flyer_filename=flyer_filename,
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event


# ── GET /events/
@app.get("/events/", response_model=List[schemas.EventOut])
def list_events(db: Session = Depends(get_db)):
    """Return a list of all events."""
    events = db.query(models.Event).all()
    return events


# ── POST /events/{event_id}/rsvp
@app.post("/events/{event_id}/rsvp", response_model=schemas.RSVPOut, status_code=201)
def rsvp_to_event(
    event_id: int,
    name: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(get_db),
):
    """RSVP to an existing event by event ID."""
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

   
    existing = (
        db.query(models.RSVP)
        .filter(models.RSVP.event_id == event_id, models.RSVP.email == email)
        .first()
    )
    if existing:
        raise HTTPException(
            status_code=400, detail="This email has already RSVP'd to this event"
        )

    rsvp = models.RSVP(name=name, email=email, event_id=event_id)
    db.add(rsvp)
    db.commit()
    db.refresh(rsvp)
    return rsvp


# ── GET /events/{event_id}/rsvps 
@app.get("/events/{event_id}/rsvps", response_model=List[schemas.RSVPOut])
def get_rsvps(event_id: int, db: Session = Depends(get_db)):
    """Get all RSVPs for a specific event."""
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    return event.rsvps

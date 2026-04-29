from typing import List, Optional
from pydantic import BaseModel



class RSVPCreate(BaseModel):
    name: str
    email: str


class RSVPOut(BaseModel):
    id: int
    name: str
    email: str
    event_id: int

    class Config:
        from_attributes = True  


class EventCreate(BaseModel):
    title: str
    description: str
    date: str
    location: str


class EventOut(BaseModel):
    id: int
    title: str
    description: str
    date: str
    location: str
    flyer_filename: Optional[str] = None
    rsvps: List[RSVPOut] = []

    class Config:
        from_attributes = True

from fastapi import APIRouter, Body
from helpers.event_functions import create_event, get_events, add_multiple_events
from models.Events import EventModel


router = APIRouter()

@router.post("/events")
def add_event(event: EventModel):
    print(event)
    try:
        return create_event(event.date, event.time, event.attendees, event.timeZone, event.summary, event.userId, event.duration, event.type, event.isGroup, event.isOnline, event.direction, event.meetLink)
    except Exception as e:
        return {"error": str(e)}

@router.post("/events/multiple")
def create_multiple_events(events: list[EventModel] = Body(..., embed=True)):
  try:
      return add_multiple_events(events)
  except Exception as e:
      return {"error": str(e)}

@router.get("/events/{userId}")
def read_events(userId: str):
    try:
        return get_events(userId)
    except Exception as e:
        return {"error": str(e)}



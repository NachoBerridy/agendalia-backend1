from fastapi import APIRouter
from models.Availability import AvailabilityModel
from helpers.availability_functions import save_availability, get_availability, get_availability_with_events



router = APIRouter()

@router.post("/availability")
def create_availability(availability: AvailabilityModel):
    try:
        return save_availability(availability.userId, availability.availability, availability.overrideDates, availability.timeZone, availability.name)
    except Exception as e:
        return {"error": str(e)}
    
@router.get("/availability/{userId}")
def read_availability(userId: str):
    try:
        return get_availability(userId)
    except Exception as e:
        return {"error": str(e)}
    
@router.get("/availability/{userId}/{month}/{year}/{day}")
def read_availability_with_events(userId: str, month: int, year: int, day: int):
    try:
        return get_availability_with_events(userId, month, year, day)
    except Exception as e:
        return {"error": str(e)}
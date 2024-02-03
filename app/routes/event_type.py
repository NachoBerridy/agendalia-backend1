from fastapi import APIRouter, Depends, HTTPException, status, Query
from models.Event_Type import Event_Type_Model
from helpers.event_types_functions import save_event_type, EventTypeCreationError, get_event_types, get_event_types_by_username, get_event_type_by_link

router = APIRouter()

@router.post("/event_type")
def create_event_type(event_type: Event_Type_Model):
    try:
        return save_event_type(
                event_type.name, 
                event_type.description, 
                event_type.duration, 
                event_type.price, 
                event_type.isGroup, 
                event_type.isOnline, 
                event_type.direction, 
                event_type.meetService,
                event_type.link, 
                event_type.isActive, 
                event_type.userId
        )
    except EventTypeCreationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/event_type/{userId}")
def get_event_types_by_user(userId: str):
    try:
        return get_event_types(userId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/event_type/username/{userName}")
def event_types_by_user_name(userName: str):
    try:
        return get_event_types_by_username(userName)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/event_type/link/{userName}/{link}")
def event_type_by_link(userName: str, link: str):
    try:
        return get_event_type_by_link(userName, link)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
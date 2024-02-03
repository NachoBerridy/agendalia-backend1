from typing import List, Union, Optional
from pydantic import BaseModel

class EventModel(BaseModel):
    summary: str
    date: str
    time: str
    attendees: List[str]
    timeZone: str
    userId: str
    duration: int
    type: str
    isGroup: Optional[bool]
    isOnline: Optional[bool]
    direction: Optional[str]
    meetLink: Optional[str]


from typing import Optional
from pydantic import BaseModel

class PriceModel(BaseModel):
  amount: float
  currency: str


class Event_Type_Model(BaseModel):
    name: str
    description: str
    duration: int
    price: PriceModel
    isGroup: bool
    isOnline: bool
    direction: Optional[str]
    meetService: Optional[str]
    link: str
    isActive: bool
    userId: str

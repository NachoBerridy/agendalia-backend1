from pydantic import BaseModel, EmailStr
from typing import List, Union, Optional

class UserBase(BaseModel):
    email: EmailStr
    userName: str
    firstName: str
    lastName: str
    phoneNumber: Optional[str] = None
    isVerified: bool = False
    profession: Optional[str] = None
    token: str
    


class userLogin(BaseModel):
    email: EmailStr
    password: str
    token: str = None


from fastapi import APIRouter
from helpers.firebase_auth import *
from models.Users import UserBase, userLogin



router = APIRouter()

@router.post("/users/signup")
def register_user(user: UserBase):
    try:
        return create_user(user.token, user.userName, user.firstName, user.lastName, user.email)
    except Exception as e:
        return {"error": str(e)} 
    
@router.post("/users/signin")
def sign_in(body: dict):
    try:
        return sign_in_with_email_and_password(body['token'])
    except Exception as e:
        return {"error": str(e)}


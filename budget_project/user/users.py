from fastapi import APIRouter 
from pydantic import BaseModel, Field, EmailStr
from email_validator import validate_email, EmailNotValidError


router = APIRouter()


"""
User Dict
"""
USERS = [
    {
        "First_Name": "Bob",
        "Last_Name": "White",
        "Email": "BobWhite@test.com"
    }
]

"""
Got to test the class for when creating a new users!!!
I'm pretty sure something isn't right haha
"""
class User(BaseModel):
    first_name: str
    last_name: str 
    email: EmailStr 

    def validate_email_address(email):
        try: 
            validate_email(email)
            return True
        except EmailNotValidError as e:
            print(str(e))



@router.get("/users")
async def get_users():
    return USERS
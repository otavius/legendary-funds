from fastapi import APIRouter 
from pydantic import BaseModel, Field, EmailStr
from email_validator import validate_email, EmailNotValidError
from passlib.context import CryptContext


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
Going to need to add password for users maybe in the class of User... 
also probably add templeting for this endpoint for users 
going to use bootstrap to get the form 
"""

hash_password = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return hash_password.hash(password)

def veriry_password(plain_password: str, hashed_password: str):
    return hash_password.verify(plain_password, hashed_password)


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

@router.post("/create-user")
async def create_user(user: User):
    try: 
        if user in USERS:
            return None
        
        USERS.append(user)
    except:
        pass 
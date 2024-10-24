from fastapi import FastAPI
from backend.user import users

app = FastAPI()

app.include_router(users.router)

@app.get("/")
async def get_index():
    return {"Message": "Building my Budget"}
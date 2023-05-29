from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None

users = []  

@app.get("/users", response_model=List[User])
async def get_user():
    return users

@app.get("/users/{user_id}")
async def get_user(user_id:int = Path(..., description="The ID of the user you'd like to view", gt=0)):
    return users[user_id]

@app.post('/users')
async def create_user(user: User):
    users.append(user)
    return user
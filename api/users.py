from typing import Optional, List
import fastapi 
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

from api.utils.users_util import get_users, create_user, get_user, get_user_by_email
from api.utils.courses_util import get_user_courses
from pydantic_schemas.course_schema import Course
from pydantic_schemas.user_schema import User, UserCreate
from db.db_setup import get_db

router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def read_users( skip: int = 0, limit: int = 100, db: Session = fastapi.Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = fastapi.Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@router.get("/users/{user_id}", response_model=User, status_code=200)
async def read_user(user_id: int, db: Session = fastapi.Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/users/{user_id}/courses", response_model=List[Course])
async def read_user_courses(user_id: int, db: Session = Depends(get_db)):
    courses = get_user_courses(db=db, user_id=user_id)
    if courses is None:
        raise HTTPException(status_code=404, detail="User not found")
    return courses
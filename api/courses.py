import fastapi
from fastapi import Depends
from typing import Optional, List
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException 

from db.db_setup import get_db
from api.utils.courses_util import get_courses, create_course, get_course
from pydantic_schemas.course_schema import Course, CourseCreate

router = fastapi.APIRouter()

@router.get("/courses", response_model=list[Course])
async def read_courses(db: Session = Depends(get_db)):
    courses = get_courses(db=db)
    return courses

@router.post("/courses", response_model=Course, status_code=201)
async def create_new_course( course: CourseCreate, db: Session = Depends(get_db)):
    return create_course(db=db, course=course)

@router.get("/courses/{course_id}")
async def read_course( course_id: int, db: Session = Depends(get_db)):
    course = get_course(db=db, course_id=course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.patch("/courses/{course_id}")
async def update_course():
    return {"courses": []}


@router.delete("/courses/{course_id}")
async def delete_course():
    return {"courses": []}


@router.get("/courses/{course_id}/sections")
async def read_course_sections():
    return {"courses": []}
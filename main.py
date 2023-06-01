from fastapi import FastAPI

from api import users, sections, courses
from db.db_setup import engine
from db.models import user_model, course_model 

user_model.Base.metadata.create_all(bind=engine)
course_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router) 
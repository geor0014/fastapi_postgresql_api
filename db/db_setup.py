from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "{driver}://{userame}:{password}@localhost:{port}/{data_base_name}"
# example: SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/online_courses"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
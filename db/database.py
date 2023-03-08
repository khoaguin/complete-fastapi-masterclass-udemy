from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi-practice.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()  # will be used to create our db Models


def get_db():
    """
    Anytime we perform any operations on the db, we create a local
    session, yield it and close it when we are done.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

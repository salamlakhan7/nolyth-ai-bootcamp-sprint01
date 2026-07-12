# database.py
# SQLite engine + session setup - swap-in-ready for Postgres later
# (just change SQLALCHEMY_DATABASE_URL and add psycopg2 to requirements)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./sprint01.db"

# check_same_thread=False is SQLite-specific - FastAPI can use multiple threads per request
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Dependency - yields a DB session per request, closes it after."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

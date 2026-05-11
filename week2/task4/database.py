import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from logger import get_logger

logger = get_logger(__name__)

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@localhost:"
    f"{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)

engine = create_engine(URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        logger.info("Database connection opened")
        yield db
    except Exception as exc:
        logger.error("Database error: %s", exc)
        raise
    finally:
        db.close()
        logger.info("Database connection closed")

import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO, filename= 'log.log', format="%(asctime)s - %(levelname)s - %(message)s")


load_dotenv(Path(__file__).resolve().parent / ".env")

# postgresql://{user}:{password}@{host}:{port}/{db_name}
URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"


engine = create_engine(URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#base class
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        logging.info("Database connection opened") 
        yield db
    except Exception as e:
        logging.error(f"Database error: {e}") 
        raise
    finally:
        db.close() 
        logging.info("Database connection closed") 

        
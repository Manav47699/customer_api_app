from fastapi import FastAPI

import database
import models
import router
from logger import get_logger

logger = get_logger(__name__)

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="ClassicModels Concurrency Dashboard", version="1.0")
app.include_router(router.router)


@app.get("/")
def root():
    logger.info("Root endpoint accessed")
    return {"message": "Task3 API is running"}

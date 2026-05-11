from fastapi import FastAPI
import models, database, router

# Create the tables in the DB
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(router.router)
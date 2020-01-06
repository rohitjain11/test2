from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine
import celery_worker 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# Dependency



    
@app.get("/range/")
def add_value(start: int, end: int):

    mytask = celery_worker.add_data(start=start, end=end)
    return mytask
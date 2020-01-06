from celery import current_task
from sqlalchemy.orm import Session
import models, time
from database import SessionLocal, engine
from celery.result import AsyncResult
from celery import Celery


db = SessionLocal()
        

celery_app = Celery('add', backend="db+postgresql://postgres:postgres@localhost/postgres", broker='amqp://localhost//')
# task data will be saved in postgresql database


def add_data(start: int, end: int):
    #if you execute this without delay it will take much time to send response
    # but by delay it will run the process of saving data in back end
    add.delay(start, end)
    return "task done"
        
  
#by using this cammand in terminal you can see process of celery "celery -A celery_worker worker --loglevel=info"
# must be execute in same location where this file is located
  
@celery_app.task
def add(start, end):
    for i in range(start, end):
        a = i
        b = i+5
        c = a+b
        db_add = models.Add(val1=a, val2=b, sum=c)
        db.add(db_add)
        time.sleep(3)
    db.commit()
    db.refresh(db_add)



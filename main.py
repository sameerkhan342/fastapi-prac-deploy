# from fastapi import FastAPI
# from .db import engine
# from . import models
# from .routers import auth

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI(title="PDF to Audio Study App Backend")

# app.include_router(auth.router)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class dataModel(BaseModel):
    name:str
    age:int

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/info')
def get_info(data: dataModel):
    return {"your data": data}

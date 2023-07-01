from fastapi import FastAPI
from app.schemas import User
from database.firebase import Database

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

@app.post("/users/")
def create_user(users: User):
    data_dict = dict(users)
    Database().create(collection='users', document='2', data=data_dict)
    return users

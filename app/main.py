from fastapi import FastAPI
from app.models import User

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

@app.post("/users/")
def create_user(users: User):
    return users

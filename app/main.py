from fastapi import FastAPI
from app.schemas import User
from database.firebase import Firestore
from app.utils import hash_password

app = FastAPI()
database = Firestore()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

@app.post("/users/create/")
def create_user(users: User):
    user = dict(users)
    user['password'] = hash_password(user['password'])

    database.create(collection='users', data=user)
    return {'user': 'Registered user.'}


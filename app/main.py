from fastapi import FastAPI
from app.schemas import User
from database.firebase import Firestore

app = FastAPI()
database = Firestore()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

@app.post("/users/")
def create_user(users: User):
    database.create(collection='users', data=dict(users))
    return {'user': 'Registered user.'}

@app.get('/users/{user_id}')
def read_user(user_id: str):
    data = database.read(collection='users', document=user_id)
    if data.exists:
        return {'user': data.to_dict()}
    else:
        return {'user': 'User does not exists.'}

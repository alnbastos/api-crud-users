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

@app.get('/users/')
def read_user():
    list_users = list()

    for user in database.read_all('users'):
        dict_user = user.to_dict()
        dict_user['id'] = user.id

        list_users.append(dict_user)

    return {'user': list_users}

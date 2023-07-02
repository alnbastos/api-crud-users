import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import os
file_path = os.path.dirname(os.path.abspath(__file__))
full_directory = os.path.join(file_path, 'key_database.json')

# Use a service account.
cred = credentials.Certificate(full_directory)
firebase_admin.initialize_app(cred)

class Firestore:
    def __init__(self):
        self.db = firestore.client()


    def create(self, collection, data):
        return self.db.collection(collection).add(data)


    def read(self, collection, document):
        return self.db.collection(collection).document(document).get()


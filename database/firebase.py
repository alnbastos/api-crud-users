import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import os
file_path = os.path.dirname(os.path.abspath(__file__))
full_directory = os.path.join(file_path, 'key_database.json')

# Use a service account.
cred = credentials.Certificate(full_directory)
firebase_admin.initialize_app(cred)

class Database:
    def __init__(self):
        self.db = firestore.client()


    def create(self, collection, document, data):
        doc_ref = self.db.collection(collection).document(document)
        doc_ref.set(data)



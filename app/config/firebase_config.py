import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os.path

def initialize_app():
    cred = credentials.Certificate(os.path.join(os.path.dirname(__file__), 'credentials.json'))
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://<DATABASE_NAME>.firebaseio.com'
    })

initialize_app()

db = firestore.client()

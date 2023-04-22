import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore import Client as FirestoreClient


cred = credentials.Certificate('firebase-credentials.json')
firebase_admin.initialize_app(cred,  {
    'databaseURL': 'https://plants-buddy.firebaseio.com'
})

db: FirestoreClient = firestore.client()
import firebase_admin
from firebase_admin import credentials, firestore
# from firebase_admin.firestore import client,
from dotenv import dotenv_values
import json
# from google.cloud import firestore, FieldFilter

# client()
config = dotenv_values()

service = json.loads(config['SERVICE_ACCOUNTED'])

try:
    cred = credentials.Certificate(service)
    firebase_admin.initialize_app(cred)
    print('Firebase config succesful')
except Exception as e:
    print(str(e))

# db = firestore.client()
# doc_ref = db.collection("waitlist")

# doc = doc_ref.get()
# if doc.exists:
#     print(f"Document data: {doc.to_dict()}")
# else:
#     print("No such document")

# print(trial)
def check_email_exists(email: str):
    # db = firestore.client()
    # ref = db.collection('waitlist')
    ref = firestore.client().collection('waitlist')

    snapshot = ref.where('Email', '==', email).get()
    print('type of snap', type(snapshot))
    # snapshot = ref.stream()
    # print(snapshot)
    if not snapshot:
        print(f"No such document")
        # raise Exception(f"User with email - {email} already exists")
    
    for snap in snapshot:
        print(snap.to_dict())


check_email_exists('oyindamolatemi94@gmail.com')
# check_email_exists('obaff@gmail.com')
# 

stay = []
# stay.
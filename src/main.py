from fastapi import FastAPI

from firebase_admin import credentials
from dotenv import dotenv_values
import firebase_admin
import json

from routers import router


config = dotenv_values()

app = FastAPI()

app.include_router(router.router, tags=['Newsletter'], prefix='/newsletter')

# firebase service account creds to connect to firestore 
service = json.loads(config['SERVICE_ACCOUNT'])


try:
    cred = credentials.Certificate(service)
    firebase_admin.initialize_app(cred)
    print('Firebase config succesful')
except Exception as e:
    print(str(e))


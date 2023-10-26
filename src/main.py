import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import dotenv_values
import json
from fastapi import FastAPI, HTTPException, status

from modules import check_email, generate_code
from schemas import schema
from routers import router

config = dotenv_values()

app = FastAPI()

service = json.loads(config['SERVICE_ACCOUNT'])

try:
    cred = credentials.Certificate(service)
    firebase_admin.initialize_app(cred)
    print('Firebase config succesful')
except Exception as e:
    print(str(e))

collection = firestore.client().collection('newsletter')

@app.get('/check')
def check_email_extr(email: str):
    pass


@app.get('/all')
def get_all_email():
    return router.users(firestore)


@app.post('/new')
def join(request: schema.User):

    if check_email.check_email_exists(request.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail=f'The email - {request.email} already exists')

    code = generate_code.create_code()
    new_user = {
        'nickname': request.nickname,
        'email': request.email,
        'referral_code': code
    }

    collection.add(new_user)

    return new_user


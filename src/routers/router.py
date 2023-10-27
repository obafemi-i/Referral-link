from fastapi import APIRouter, HTTPException, status
from firebase_admin import firestore

from schemas import schema
from modules import check_email, generate_code

router = APIRouter()


@router.get('/users')
def users():

    collection = firestore.client().collection('newsletter')

    snapshot = collection.get()
    users = []

    if len(snapshot) == 0:
        print('Collection is empty')
        return {'message': 'Collection is empty'}
    else:
        for snap in snapshot:
            users.append(snap.to_dict())
        return users
    

@router.post('/join')
def join(request: schema.User):
    collection = firestore.client().collection('newsletter')

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
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
    

@router.post('/join', response_model=schema.Joined)
def join(request: schema.User):
    collection = firestore.client().collection('newsletter')

    if check_email.check_email_exists(request.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail=f'The email - {request.email} already exists')

    base_url = 'https://example.com'
    
    code = generate_code.create_code()

    referral_link = f'{base_url}/?nickname={request.nickname}/?code={code}'

    new_user = {
        'nickname': request.nickname,
        'email': request.email,
        'referral_code': code,
        'referral_link': referral_link
    }
    
    print(referral_link)

    collection.add(new_user)

    # return new_user['referral_link']
    return {'message': f'Thank you for sigining up for the newsletter, your referral code is{new_user["referral_link"]}'}
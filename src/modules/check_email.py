from firebase_admin import firestore

def check_email_exists(email: str):
    db_ref = firestore.client().collection('newsletter')

    snapshot = db_ref.where('Email', '==', email).get()

    if snapshot:
        raise Exception(f'The email - ${email} already exists')
    
    

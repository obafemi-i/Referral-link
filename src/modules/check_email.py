from firebase_admin import firestore

def check_email_exists(email: str):
    db_ref = firestore.client().collection('newsletter')

    snapshot = db_ref.where('email', '==', email).get()

    if snapshot:
        return True

    

from firebase_admin import firestore

import string
import random

def create_code():
    db_ref = firestore.client().collection('newsletter')

    characters = string.ascii_letters + string.digits

    code = 'Z' + ''.join(random.choices(characters, k=4))

    snapshot = db_ref.where('Code', '==', code).get()

    if snapshot:
        create_code()

    return code
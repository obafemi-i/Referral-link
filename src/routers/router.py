from fastapi import APIRouter


# , response_model=list[schema.AllUsers]
def users(firestore):
    collection = firestore.client().collection('newsletter')

    snapshot = collection.get()
    users = []

    if len(snapshot) == 0:
        print('Collection is empty')
    else:
        for snap in snapshot:
            users.append(snap.to_dict())
        return users
    

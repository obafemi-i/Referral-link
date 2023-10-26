from pydantic import BaseModel

class AllUsers(BaseModel):
    Email: str
    
    class config():
        orm_mode = True


class User(BaseModel):
    email: str
    nickname: str

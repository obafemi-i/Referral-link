from pydantic import BaseModel

class Users(BaseModel):
    Email: str
    
    class config():
        orm_mode = True


class User(BaseModel):
    email: str
    nickname: str

class Joined(BaseModel):
    referral_link: str

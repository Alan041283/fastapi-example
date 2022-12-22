from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint

'''
class Post(BaseModel):
    title: str
    content:str
    #campo non opzionale ma che se non inserirsco mette valore predefinito
    published: bool = True
    #test: str = True
    #campo opzionale
    #rating: Optional[int] = None


#best practice utilizzare classe per ogni operazioni in modo da poter personalizzare la struttura


class CreatePost(BaseModel):
    title: str
    content: str
    published: bool = True


class UpdatePost(BaseModel):
    pass
'''

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass
    #published: bool

#per non fare vedere password nella risposta della post
class OutUser(BaseModel):
    id: int
    email:EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

#posso anche evitare che la risposta non comprenda tuitti i campo se alcuni, quelli automatici, li voglio nascondere
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: OutUser
    ####votes: Vote
    class Config:
        orm_mode = True

#aggiungo allo schema post anche il vote
class PostOut(BaseModel):
    Post: Post
    votes: int
    class Config:
        orm_mode = True






class CreateUser(BaseModel):
    email:EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]=None


class Vote(BaseModel):
    post_id: int
    dir : conint(le=1)

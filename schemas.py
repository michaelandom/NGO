from pydantic import BaseModel
from typing import List, Optional


class User(BaseModel):
    name: str
    email: str
    password: str


class Blog(BaseModel):
    title: str
    body: str


class BlogBase(Blog):
    class Config():
        orm_mode = True


class showUser(BaseModel):
    name: str
    email: str
    blogs: List[BlogBase]

    class Config():
        orm_mode = True


class showUserBase(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True


class showBlog(BaseModel):
    title: str
    body: str
    creator: showUserBase

    class Config():
        orm_mode = True


class Login(BaseModel):
    userName: str
    passWord: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

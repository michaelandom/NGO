from pydantic import BaseModel
from typing import List, Optional


class CreateUser(BaseModel):
    name: str
    email: str
    password: str
    type: str
    region: str


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    type: str
    region: str


class Blog(BaseModel):
    title: str
    body: str
    trainingStartDate: str
    trainingEndDate: str
    trainingVenue: str
    kindOfTraining: str
    DUPRole: str
    region: str
    RHB: str
    zone: str
    woreda: str
    hospitals: str
    HC: str
    HP: str
    universities: str
    partners: str
    FMOH: str
    EPHI: str
    other: str
    totalNumber: int


class BlogBase(Blog):
    class Config():
        orm_mode = True


class showUser(BaseModel):
    name: str
    email: str
    type: str
    region: str
    blogs: List[BlogBase]

    class Config():
        orm_mode = True


class showUserBase(BaseModel):
    name: str
    email: str
    type: str
    region: str

    class Config():
        orm_mode = True


class showBlog(BaseModel):
    title: str
    body: str
    trainingStartDate: str
    trainingEndDate: str
    trainingVenue: str
    kindOfTraining: str
    DUPRole: str
    region: str
    RHB: str
    zone: str
    woreda: str
    hospitals: str
    HC: str
    HP: str
    universities: str
    partners: str
    FMOH: str
    EPHI: str
    other: str
    totalNumber: int
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
    id: Optional[int] = None

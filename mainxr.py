from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.get("/")
def index():
    return {"data": {"message": "index page"}}


@app.get("/blog")
def published(limit: int, publish: bool):
    if publish:
        return {"data": f"{limit} publish blog list"}
    else:
        return {"data": f"{limit} all= blog list"}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "unpublished"}


@app.get("/blog/{id}")
def about(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id: int):
    return {"data": ["a", "b", "c"]}


@app.post("/blog")
def createBlog(blogBody: Blog):
    return blogBody

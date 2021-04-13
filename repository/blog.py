from fastapi import status, HTTPException
from sqlalchemy.orm import Session
import models, schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create_blog(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_blog(id, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"cant find blog with id {id}")
    return blogs

def delete_blog(id, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id)
    if not blogs.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"cant find blog with id {id}")
    blogs.delete(synchronize_session=False)
    db.commit()
    return {"data": "deleted"}

def delete_blog(id, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id)
    if not blogs.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"cant find blog with id {id}")
    blogs.delete(synchronize_session=False)
    db.commit()
    return {"data": "deleted"}

def update_blog(id, request: schemas.Blog, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id)
    if not blogs.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"cant find blog with id {id}")
    # blogs.update(request)
    blogs.update({"title": request.title, "body": request.body}, synchronize_session=False)
    db.commit()
    return "updated"
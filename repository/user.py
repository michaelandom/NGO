from fastapi import status, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from hashing import Hash


def get_all(db: Session):
    blogs = db.query(models.User).all()
    return blogs


def create_user(request: schemas.Blog, db: Session):
    hashedPassword = Hash.get_password_hash(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(id, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"cant find user with id {id}")
    return user


def delete_user(id, db: Session):
    users = db.query(models.User).filter(models.User.id == id)
    if not users.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"cant find user with id {id}")
    users.delete(synchronize_session=False)
    db.commit()
    return {"data": "deleted"}


def update_user(id, request: schemas.User, db: Session):
    users = db.query(models.User).filter(models.User.id == id)
    if not users.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"cant find user with id {id}")
    users.update({"name": request.name, "email": request.email, "password": request.password},
                 synchronize_session=False)
    db.commit()
    return "updated"

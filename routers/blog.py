from fastapi import APIRouter,Depends, status
import schemas
from database import get_db
from sqlalchemy.orm import Session
from typing import List
from repository import blog
from oauth2 import get_current_user
router = APIRouter(
    prefix="/blog",
    tags=["training"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.showBlog)
def create_Blog(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.create_blog(request, db,current_user)


@router.get("/", response_model=List[schemas.showBlog])
def get_Blog(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db,current_user)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.showBlog)
def get_Id_Blog(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return  blog.get_blog(id, db)

@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete_Blog(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.delete_blog(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_Blog(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.update_blog(id, request, db)

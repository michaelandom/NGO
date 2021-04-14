from fastapi import APIRouter, Depends, status
import schemas
from database import get_db
from sqlalchemy.orm import Session
from fastapi_pagination import Page,add_pagination,paginate

from repository import user
from oauth2 import get_current_user
router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.showUser)
def create_User(request: schemas.CreateUser, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return user.create_user(request, db)


@router.get("/", response_model=Page[schemas.showUser])
def get_All_User(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return paginate(user.get_all(db))


@router.get("/{id}", response_model=schemas.showUser)
def get_User(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return user.get_user(id, db)

@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete_Blog(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return user.delete_user(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_Blog(id, request: schemas.User, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return user.update_user(id, request, db)
add_pagination(router)
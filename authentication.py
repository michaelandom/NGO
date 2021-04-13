from fastapi import APIRouter,Depends, status,HTTPException
import models
from database import get_db
from sqlalchemy.orm import Session
from hashing import Hash
from tokendata import create_access_token
from fastapi.security import  OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/login",
    tags=["authentication"]
)

@router.post("/", status_code=status.HTTP_200_OK)
def Login(request: OAuth2PasswordRequestForm =Depends(), db: Session = Depends(get_db)):
    user=db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid Credentials")
    if not Hash.verify_password(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="password incorrect")

    access_token = create_access_token(data={"sub": user.email,"id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}


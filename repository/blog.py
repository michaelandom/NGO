from fastapi import status, HTTPException
from sqlalchemy.orm import Session
import models, schemas


def get_all(db: Session,current_user: schemas.User):
    blogs = db.query(models.Blog).filter(models.Blog.user_id == current_user.id).all()
    return blogs


def create_blog(request: schemas.Blog, db: Session, current_user: schemas.User):
    new_blog = models.Blog(title=request.title, body=request.body,
                           trainingStartDate=request.trainingStartDate,
                           trainingEndDate=request.trainingEndDate,
                           trainingVenue=request.trainingVenue,
                           kindOfTraining=request.kindOfTraining,
                           DUPRole=request.DUPRole,
                           region=request.region,
                           RHB=request.RHB,
                           zone=request.zone,
                           woreda=request.woreda,
                           hospitals=request.hospitals,
                           HC=request.HC,
                           HP=request.HP,
                           universities=request.universities,
                           partners=request.partners,
                           FMOH=request.FMOH,
                           EPHI=request.EPHI,
                           other=request.other,
                           totalNumber=request.totalNumber,
                           user_id=current_user.id)
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


def update_blog(id, request: schemas.Blog, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id)
    if not blogs.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"cant find blog with id {id}")
    # blogs.update(request)
    blogs.update({
        "title": request.title,
        "body": request.body,
        "trainingStartDate":request.trainingStartDate,
        "trainingEndDate":request.trainingEndDate,
        "trainingVenue":request.trainingVenue,
        "kindOfTraining":request.kindOfTraining,
        "DUPRole":request.DUPRole,
        "region":request.region,
        "RHB":request.RHB,
        "zone":request.zone,
        "woreda":request.woreda,
        "hospitals":request.hospitals,
        "HC":request.HC,
        "HP":request.HP,
        "universities":request.universities,
        "partners":request.partners,
        "FMOH":request.FMOH,
        "EPHI":request.EPHI,
        "other":request.other,
        "totalNumber":request.totalNumber,
    }, synchronize_session=False)
    db.commit()
    return "updated"

from fastapi import FastAPI
import models
from database import engine
from routers import user,blog
import authentication


models.Base.metadata.create_all(engine)
app = FastAPI()


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

#
# @app.post("/blog", status_code=status.HTTP_201_CREATED,tags=["blog"],response_model=schemas.showBlog)
# def createBlog(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog
#
#
# @app.get("/blog",response_model=List[schemas.showBlog],tags=["blog"])
# def getBlog(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs
#
#
# @app.get("/blog/{id}", status_code=status.HTTP_200_OK,response_model=schemas.showBlog,tags=["blog"])
# def getBlog(id, db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blogs:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"cant find blog with id {id}")
#     return blogs
#
# @app.delete("/blog/{id}", status_code=status.HTTP_202_ACCEPTED,tags=["blog"])
# def deleteBlog(id, db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blogs.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"cant find blog with id {id}")
#     blogs.delete(synchronize_session=False)
#     db.commit()
#     return {"data":"deleted"}
#
# @app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED,tags=["blog"])
# def updateBlog(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     blogs =db.query(models.Blog).filter(models.Blog.id == id)
#     if not blogs.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"cant find blog with id {id}")
#     #blogs.update(request)
#     blogs.update({"title": request.title, "body": request.body},synchronize_session=False)
#     db.commit()
#     return "updated"



# @app.post("/user", status_code=status.HTTP_201_CREATED,response_model=schemas.showUser,tags=["user"])
# def createUser(request: schemas.User, db: Session = Depends(get_db)):
#     hashedPassword=Hash.get_password_hash(request.password)
#     new_user = models.User(name=request.name, email=request.email, password= hashedPassword)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
#
# @app.get("/user",response_model=List[schemas.showUser],tags=["user"])
# def getAllUser(db: Session = Depends(get_db)):
#     blogs = db.query(models.User).all()
#     return blogs
#
# @app.get("/user/{id}",response_model=schemas.showUser,tags=["user"])
# def getUser(id,db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"cant find user with id {id}")
#
#     return user

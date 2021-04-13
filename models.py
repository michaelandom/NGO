from database import Base
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    trainingStartDate = Column(String)
    trainingEndDate = Column(String)
    trainingVenue = Column(String)
    kindOfTraining = Column(String)
    DUPRole = Column(String)
    region = Column(String)
    RHB = Column(String)
    zone = Column(String)
    woreda = Column(String)
    hospitals = Column(String)
    HC = Column(String)
    HP = Column(String)
    universities = Column(String)
    partners = Column(String)
    FMOH = Column(String)
    EPHI = Column(String)
    other = Column(String)
    totalNumber = Column(Integer)
    user_id= Column(Integer, ForeignKey("user.id"))
    creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    type = Column(String)
    region = Column(String)
    blogs = relationship("Blog", back_populates="creator")


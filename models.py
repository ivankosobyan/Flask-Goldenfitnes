from sqlalchemy import Column,Integer,String,DateTime,Text
from sqlalchemy.sql import func

from db import db
class Trener(db.Model):
    id = Column(Integer,primary_key=True)
    age = Column(Integer)
    special = Column(String(100))
    name = Column(String(50))
    surname = Column(String(50))
    created_at = Column(DateTime,server_default=func.now())
    updated_at = Column(DateTime,server_onupdate=func.now())
    url_image=Column(String(250))
    description=Column(Text)


class PersonalTrening(db.Model):
    id = Column(Integer,primary_key=True)
    tipe = Column(String(200))
    datetime = Column(DateTime)
    created_at = Column(DateTime,server_default=func.now())
    updated_at = Column(DateTime,server_onupdate=func.now())

class GroupTrening(db.Model):
    id = Column(Integer,primary_key=True)
    trening = Column(String(150))
    trener = Column(String(100))
    datetime = Column(DateTime)
    created_at = Column(DateTime,server_default=func.now())
    updated_at = Column(DateTime,server_onupdate=func.now())

class User(db.Model):
    id = Column(Integer,primary_key=True)
    name = Column(String(150))
    surname =Column(String(150))
    hashed_password = Column(String(256))
    email = Column(String(45))
    telephone = Column(Integer)
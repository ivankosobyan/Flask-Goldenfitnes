from sqlalchemy import Column,Integer,String,DateTime,Text,ForeignKey,Table
from sqlalchemy.sql import func
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from db import db

grouptrening2trener = Table(
"group_trening2trener",db.Model.metadata,
Column("group_trning_id",ForeignKey("group_trening.id")),
Column("trener_id",ForeignKey("trener.id")) 

)

class Trener(db.Model):
    __tablename__ = "trener"
    id = Column(Integer,primary_key=True)
    age = Column(Integer)
    special = Column(String(100))
    name = Column(String(50))
    surname = Column(String(50))
    created_at = Column(DateTime,server_default=func.now())
    updated_at = Column(DateTime,server_onupdate=func.now())
    url_image=Column(String(250))
    description=Column(Text)
    personal_trenings = relationship("PersonalTrening",back_populates="trener")
    def __repr__(self):  # делает видимыми указаные атрибуты для простых обывателей
        return self.name +" "+self.surname + "("+ self.special +")"


class PersonalTrening(db.Model):
    __tablename__= "personal_trening"
    id = Column(Integer,primary_key=True)
    tipe = Column(String(200))
    datetime = Column(DateTime)
    created_at = Column(DateTime,server_default=func.now())
    updated_at = Column(DateTime,server_onupdate=func.now())
    trener_id = Column(Integer,ForeignKey("trener.id")) # я являюсь ссылкой для атрибута trener.id
    trener = relationship("Trener",back_populates="personal_trenings") # просканируй таблицу "Trener" на предмет объекта trener
    def __repr__(self):
        return self.tipe + " Будет проводить " + str(self.trener) + " время: " + str(self.datetime)



class GroupTrening(db.Model):
    __tablename__ = "group_trening"
    id = Column(Integer,primary_key=True)
    trening = Column(String(150))
    trener = Column(String(100))
    datetime = Column(DateTime)
    created_at = Column(DateTime,server_default=func.now())
    updated_at = Column(DateTime,server_onupdate=func.now())
    treners = relationship("Trener",secondary=grouptrening2trener)
    def __repr__(self):
        return self.trening + " проводит: " + self.trener + " время: " + str(self.datetime)

class User(db.Model,UserMixin):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True)
    name = Column(String(150))
    surname = Column(String(150))
    hashed_password = Column(String(256))
    email = Column(String(45))
    telephone = Column(Integer)
    def __repr__(self):
        return self.name +" "+ self.surname + " почта: " + self.email + " номер: " + str(self.telephone)
    

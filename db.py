from flask_sqlalchemy import SQLAlchemy
from app import app                                         
from flask_migrate import Migrate
from sqlalchemy import MetaData


convention = {
    "ix": 'ix%(column0_label)s',
    "uq": "uq%(table_name)s%(column_0_name)s",
    "ck": "ck%(table_name)s%(constraintname)s",
    "fk": "fk%(table_name)s%(column_0_name)s%(referred_table_name)s",
    "pk": "pk%(table_name)s"
}

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.db"
metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(app, metadata=metadata)

migrate = Migrate(app,db,command="db")










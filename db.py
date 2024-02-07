from flask_sqlalchemy import SQLAlchemy
from app import app                                         
from flask_migrate import Migrate

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.db"

db = SQLAlchemy(app)

migrate = Migrate(app,db,command="db")







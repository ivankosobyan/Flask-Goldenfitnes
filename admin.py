from flask_admin import Admin
from app import app
from flask_admin.contrib.sqla import ModelView
from db import db
from models import Trener,PersonalTrening,GroupTrening

admin = Admin(app, "Admin panel", template_mode="bootstrap3")

class TrenerModelView(ModelView):
    column_labels=dict(name="Имя",surname="Фамилия",special="Специализируеться на",age="Возраст",created_at="Создано в",updated_at="Данные обновлялись")
    column_editable_list=["name","surname","special","age"]
    form_excluded_columns = ["created_at","updated_at"]

class PersonalTreninModelView(ModelView):
    column_labels=dict(tipe="Направленность",created_at="Создано в",updated_at="Данные обновлялись",datetime="Расписание")
    form_excluded_columns =["created_at","updated_at"]
    column_editable_list = ["tipe","datetime"]

    
class GroupTreningModelView(ModelView):
    column_labels=dict(trener="Тренер",datetime="Расписание",trening="Тип занятия",created_at="Создано в",updated_at="Данные обновлялись")
    form_excluded_columns=["created_at","updated_at"]
    

admin.add_view(TrenerModelView(Trener, db.session))
admin.add_view(GroupTreningModelView(GroupTrening,db.session))
admin.add_view(PersonalTreninModelView(PersonalTrening,db.session))



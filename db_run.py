# from models import Trener, PersonalTrening,GroupTrening
# from db import db
# from app import app

# from datetime import datetime

# with app.app_context():
#     db.drop_all()
#     db.create_all()


# with app.app_context():
#     trener = Trener(age=23,name="Игорь",special="бокс",surname="Иванович")
#     db.session.add(trener)
#     db.session.commit()
#     trener2 = Trener(age=47,name="Артем",surname="Епифанцев",special="йога")
#     db.session.add(trener2)
#     db.session.commit()
#     trener3 = Trener(age=26,name="Егор",special="Тайский бокс",surname="Петров")
#     db.session.add(trener3)
#     db.session.commit()
#     trener4 = Trener(age=5,name="Юра",special="Хоббихорсинг",surname="Антонов")
#     db.session.add(trener4)
#     db.session.commit()

# with app.app_context():
#     treners = Trener.query.all()
#     print(treners)

# for trener in treners:
#     if  trener.age==47:
#         print(trener.name, trener.surname)

# with app.app_context():
#     personal_trening = PersonalTrening(tipe="Персональный тренинг по боксу",datetime=datetime(2024,4,23,18,30))
#     db.session.add(personal_trening)
#     personal_trening = PersonalTrening(tipe="Фитнес тренинг",datetime=datetime(2024,4,26,18,30))
#     db.session.add(personal_trening)
#     personal_trening = PersonalTrening(tipe="Фитнес тренинг",datetime=datetime(2024,3,16,19,30))
#     db.session.add(personal_trening)

#     db.session.commit()

# with app.app_context():
#     gruop_trenings = GroupTrening(trener="Георгий Васильевич Агонесян", trening="Йога",datetime=datetime(2024,1,25,13))
#     db.session.add(gruop_trenings)
#     db.session.commit()


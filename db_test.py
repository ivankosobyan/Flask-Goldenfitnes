from app import app
from models import PersonalTrening,Trener,User,GroupTrening

with app.app_context():
    test = PersonalTrening.query.all()
    print(test)

with app.app_context():
    test_2 = Trener.query.all()
print(test_2)

with app.app_context():
    test_3 = User.query.all()
print(test_3)

with app.app_context():
    test_4 = GroupTrening.query.all()
print(test_4)

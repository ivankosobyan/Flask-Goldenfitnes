from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired,Email,Length # обязательное пресутствие данных, под формат почты, фильтр длинны

class LoginForm(FlaskForm):
    email = EmailField("email",validators=[DataRequired(),Email()]) #фильтры входных данных
    password = PasswordField("Пароль", validators=[Length(8,32)])


class RegisterForm(FlaskForm):
    email = EmailField("email", validators=[DataRequired(),Email()])
    password = PasswordField("Пароль",validators=[DataRequired(),Length(8,32)])
    password_repeat = PasswordField("Пароль повторно",validators=[DataRequired(),Length(8,32)])
    
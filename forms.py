from flask_wtf import Form
from wtforms import TextField, DateField, IntegerField, \
    SelectField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class NewLetter(Form):
    title = TextField('Letter Title', validators=[DataRequired()])
    content = TextField('Letter Content', validators=[DataRequired()])
    
    


class RegisterForm(Form):
    username = TextField(
        'Username',
        validators=[DataRequired(), Length(min=4, max=25)]
    )
    email = TextField(
        'Email',
        validators=[DataRequired(), Email(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=8, max=40)])
    confirm = PasswordField(
        'Repeat Password',
        validators=[DataRequired(), EqualTo('password')]
    )


class LoginForm(Form):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

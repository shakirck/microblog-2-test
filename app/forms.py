from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField,SubmitField
from wtforms.validators import DataRequired, ValidationError, Email,EqualTo,Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField ('Username',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    password2= PasswordField('Repeat Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')

class EditProfileForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    about_me = StringField('About Me',validators=[Length(min=0,max=140)])
    submit = SubmitField('Submit')


    def validate_username(self,username):
        user= User.query.filter_by(username=username.data).first()
        if user is not None :
           raise ValidationError('Please Use different Username')

    def validate_email(self,email):
        email = User.query.filter_by(email= email.data).first()
        if email is not None:
            raise ValidationError ('Please use different Email')
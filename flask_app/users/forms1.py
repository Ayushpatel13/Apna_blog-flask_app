from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flask_app.models import User

class RegistrationForm(FlaskForm):
        username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
        email=StringField('Email',validators=[DataRequired()])
        password=PasswordField('Password',validators=[DataRequired()])
        confirm_password=PasswordField('Confirm_Password',validators=[DataRequired(),EqualTo('password')])
        submit=SubmitField('Sign Up')        
        
        def validate_username(self , username):
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username is taken')
            
        def validate_email(self , email):
            email=User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('This email is taken')
    

class LoginForm(FlaskForm):
        email=StringField('Email',validators=[DataRequired()])
        password=PasswordField('password',validators=[DataRequired()])
        remember=BooleanField('remember_me')
        submit=SubmitField('Log In')
        
class UpdateAccountForm(FlaskForm):
      
        username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
        email=StringField('Email',validators=[DataRequired()])
        picture=FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
        submit=SubmitField('Update')        
        
        def validate_username(self , username):
            if username.data!=current_user.username:
                user=User.query.filter_by(username=username.data).first()
                if user:
                    raise ValidationError('This username is taken')
            
        def validate_email(self , email):
            
            if email.data!=current_user.email:
                email=User.query.filter_by(email=email.data).first()
                if email:
                    raise ValidationError('This email is taken')
                    
    
class RequestResetForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired()])
    submit=SubmitField('Request Password Reset')
    
    def validate_email(self , email):
        user=User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('This is no account with this email')
                
    
class ResetPasswordForm(FlaskForm):
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Reset Password')
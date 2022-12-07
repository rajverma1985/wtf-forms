from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message="either @ or you missed.")])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")

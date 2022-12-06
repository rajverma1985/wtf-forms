from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
import os

SECRET_KEY = os.urandom(32)

WTF_CSRF_SECRET_KEY = 'a random string'
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message="either @ or you missed.")])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")


@app.route("/", methods=['GET', 'POST'])
def home():
    login = LoginForm()
    login.validate_on_submit()
    return render_template('login.html', form=login)


if __name__ == '__main__':
    app.run(debug=True)

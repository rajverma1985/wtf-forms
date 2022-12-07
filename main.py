from flask import Flask, render_template, request
import os
from form import LoginForm

SECRET_KEY = os.urandom(32)

WTF_CSRF_SECRET_KEY = 'a random string'
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/", methods=['GET', 'POST'])
def home():
    login = LoginForm()
    if login.validate_on_submit():
        if login.email.data == "admin@email.com" and login.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login)


if __name__ == '__main__':
    app.run(debug=True)

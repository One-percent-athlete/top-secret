from flask import Flask, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap5
from flask import Flask
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.secret_key = "password"

email="admin@email.com"

password="12345678"

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Login')
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET","POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(login_form.email.data)
        if login_form.email.data == email and login_form.password.data == password:
            return render_template("success.html")
        else: 
            return render_template("denied.html")
    return render_template('login.html', form=login_form)

# @app.route("/login/<name>")
# def render_page():

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     form = LoginForm()
#     if form.validate_on_submit():
#         return redirect('/success')
#     return render_template('submit.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

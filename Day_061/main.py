from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class LoginForm(FlaskForm):
    email = StringField(
        label='Email',
        validators=[
            DataRequired(message="Email is required"),
            Length(max=60, message="Email cannot exceed 60 characters"),
            Email(message="Invalid email address format.")
        ]
    )
    password = PasswordField(
        label='Password',
        validators=[
            DataRequired(message="Password is required"),
            Length(min=8, message="Password is too short. Minimum 8 characters expected.")
        ]
    )
    submit = SubmitField(label='Log In')

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return redirect('/success')
        else:
            return redirect('/denied')
    return render_template('login.html', form=login_form)

@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/denied")
def denied():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)

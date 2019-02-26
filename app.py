from flask import Flask, request, redirect, render_template
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

from flask_wtf import FlaskForm
from forms import RegistrationForm
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = "soooo-secret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()



#root directory
@app.route('/')
def redirect_to_register():
    '''redirect user to register a new account'''
    return redirect('/register')


#register directory
@app.route('/register', methods =["GET","POST"])
def show_register_form():
    '''display registration form and handle new user registration'''
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return redirect('secret')

    else:
        return render_template('registration_form.html',form=form)





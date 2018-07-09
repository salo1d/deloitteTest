from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///deloiteTest.db', echo=True)
 
app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('log_in.html')
    else:
        return render_template('logged_in.html')

@app.route('/login', methods=['POST'])
def do_login():
 
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
 
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()

    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()
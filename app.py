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

@app.route("/deleteUser", methods=['POST'])
def delete_user():

    POST_USERNAME = str(request.form['username_to_delete'])
    POST_PASSWORD = str(request.form['password_d'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    user_to_delete = query.first()

    if user_to_delete:
        s.delete(user_to_delete)
        s.commit()
    else:
        flash('no user ' + POST_USERNAME)
    return home()


@app.route("/addUser", methods=['POST'])
def addUser():

    POST_USERNAME = str(request.form['username_to_add'])
    POST_PASSWORD = str(request.form['password_a'])

    Session = sessionmaker(bind=engine)
    s = Session()
    user_to_add = User(POST_USERNAME, POST_PASSWORD)
    s.add(user_to_add)
    s.commit()
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
 

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.debug = True
    app.run(host='0.0.0.0', port=1234)
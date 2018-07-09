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

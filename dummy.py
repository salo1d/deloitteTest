import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('sqlite:///deloiteTest.db', echo=True)

#below is line is used for PostgreSQL
#engine = create_engine('postgresql://user:password@localhost:5432/deloitte', echo=True)

 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
user = User("admin","password")
session.add(user)
 
# commit the record the database
session.commit()
 
session.commit()
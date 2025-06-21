# project/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv 
from flask_migrate import Migrate

# load environment variables
load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
Migrate(app,db)

# import models after db exists
from project.models import Category, Contact


with app.app_context():
    
    db.create_all()  # first create all tables if they don't exist
    
    # then seed categories (only if table is empty)
    if Category.query.count() == 0:
        default_categories = ["Family", "Friends", "Work", "Emergency", "Services", "Others"]
        for name in default_categories:
            db.session.add(Category(name=name))
        db.session.commit()



# import views after app is created 
from project import views, models

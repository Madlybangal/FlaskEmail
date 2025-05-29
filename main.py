
# # SQLAlchemy, a powerful library that makes working with databases 
# # easier. SQLAlchemy provides an Object Relational Mapper (ORM), 
# # allowing developers to interact with databases using Python code 
# # instead of raw SQL.
# # create a flask_app instance

        
from flask import Flask, render_template, request, redirect, url_for,flash
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String

import os
import urllib.parse
from sqlalchemy import text
app = Flask(__name__)
print("Secret Key: ",os.urandom(24))
app.secret_key=os.urandom(24)
# In a Python Flask application, a secret key is a crucial 
# component used for various security-related functions, 
# particularly for signing cookies and protecting sessions. 
# It helps ensure that the data stored in cookies cannot be 
# tampered with by clients.
# Here are some key points about the secret key in a Flask 
# application:
# Session Management: Flask uses the secret key to sign 
# session cookies. This ensures that the data stored in the 
# session cannot be altered by the client without detection.
# CSRF Protection: If you are using Flask-WTF or similar 
# libraries, the secret key is used to protect against 
# Cross-Site Request Forgery (CSRF) attacks by signing 
# CSRF tokens.
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=ASMITA_2016\MSSQLSERVER2022;"
    "DATABASE=flask_sqlproject;"
    "Trusted_Connection=yes;"
)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={params}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# The SQLAlchemy object is created with the Flask app instance,
# allowing it to manage the database connection and ORM
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

@app.route('/')
def index():
    users = Users.query.all()
    return render_template('index.html', users=users)
@app.route('/manage', methods=['POST'])
def manage_users():
    action = request.form.get('action')
    if action == 'Add':
        username = request.form.get('username')
        email = request.form.get('email')
        if username and email:
            new_user = Users(username=username, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash(f"Added user: {username} with email: {email}", "success")
    elif action == 'Delete':
        email = request.form.get('email')
        print(" email:\n ", email)
        if email:
            item = Users.query.filter_by(email=email).first()
            if item:
                db.session.delete(item)
                db.session.commit()
                flash(f"Deleted user with email: {email}", "success")
            else:
                flash(f"No user found with email: {email}", "error")
    return redirect(url_for('index'))

if __name__ == '__main__':
     app.run(debug=True)
     
from flask import Flask
import os

class Config:

    # SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://@<ASMITA_2016\MSSQLSERVER2022>/<flask_sqlproject>?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes'
    # connection_string= "mssql+pyodbc://@<ASMITA_2016\MSSQLSERVER2022>/<flask_sqlproject>?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI= 'mssql+pyodbc:///?odbc_connect=Driver={ODBC Driver 17 for SQL Server};Server=ASMITA_2016\MSSQLSERVER2022;Database=flask_sqlproject;Trusted_Connection=yes;'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
#     return app
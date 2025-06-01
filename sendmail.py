from flask import Flask, request
from flask_mail import Mail
import json
import os
with open('config.json', 'r') as f:
    params = json.load(f)['params']
app = Flask(__name__)
# you have to create app password in your gmail account
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password'],
    
)
print("Gmail id: ", params['gmail-user'])
print("Gmail password: ", params['gmail-password'])
message="This is Somu here."
mail=Mail(app)
with app.app_context():
    # Send an email
    mail.send_message('New messdage from Somu ',
                  sender='soumyendu.pc@gmail.com',
                  recipients=['pc_soumyendu@yahoo.co.in'],
                  body=message+"\n"
                  )

from flask_mail import Message
from flask import url_for
from . import mail

def send_confirmation_email(user):
    token = user.get_reset_token()
    msg = Message('Confirm Your Account', 
                  sender='noreply@demo.com', 
                  recipients=[user.email])
    
    msg.body = f'''To confirm your account, visit the following link:
{url_for('auth.confirm_email', token=token, _external=True)}
If you did not make this request, please ignore this email.
'''

    mail.send(msg)
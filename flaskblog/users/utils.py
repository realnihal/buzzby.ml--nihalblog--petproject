import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.

You can go ahead and login with your credentails, to experience our services. Check out the news page for upto date stories on different topics from different news sources. Post new stories everyday, for other users to read. 

Enjoy,
Nihal Puram
Creator
Buzzby
'''
    mail.send(msg)



def send_mail_register(user):
    msg = Message('Thank you for registering with us',
                  sender='noreply@gmail.com',
                  recipients=[user.email])
    msg.body = f'''Thank you For registering your account with us:
If you did not make this request then please contact support.

Buzzby
'''
    mail.send(msg)
import flask_mail
from project.settings import project

gmail_adress = "arzon.art125@gmail.com"

project.config['MAIL_SERVER'] = 'smtp.gmail.com'
project.config['MAIL_PORT'] = 587
project.config['MAIL_USE_TLS'] = True
project.config['MAIL_USE_SSL'] = False
project.config['MAIL_USERNAME'] = gmail_adress
project.config['MAIL_PASSWORD'] = 'qwvq jzxv kqzt iztv'

mail = flask_mail.Mail(project)
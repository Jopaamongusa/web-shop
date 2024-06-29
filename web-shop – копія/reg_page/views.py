import flask
from .models import Users
from project.settings import DATABASE
import os
import json
from sqlalchemy import create_engine
# from flask_login import current_user

def render_reg():
    path_json = os.path.abspath(__file__ + "/../../static/reg_page/json/data.json")
    with open(path_json, "r", encoding="utf-8") as file:
        data_dict = json.load(file)

    if flask.request.method == 'POST':
        if flask.request.form['name'] == 'Artem':
            is_admin = True
        else:
            is_admin = False
        print(flask.request.form)
        users = Users(
            name = flask.request.form['name'],
            email = flask.request.form['email'],
            password = flask.request.form['password'],
            is_admin = is_admin
        )
        
        DATABASE.session.add(users)
        DATABASE.session.commit()
        return flask.redirect('/')
        
    return  flask.render_template(template_name_or_list= "reg.html", body = data_dict)#, is_auth= current_user.is_authenticated

from flask import request, redirect, render_template
from reg_page.models import Users
import flask_login 
import os, flask, json
# from project.settings import login_manager
from flask_login import login_user, current_user
from project.login_manager import login_manager
import json 

def show_authorization():
    print(0)
    path_json = os.path.abspath(__file__ + "/../../static/log_page/json/data.json")
    with open(path_json, "r", encoding="utf-8") as file:
        data_dict = json.load(file)
        
    if request.method == 'POST':
        for user in Users.query.filter_by(name = flask.request.form["name"]):
            if user.password == flask.request.form["password"]:
                login_user(user)
                return flask.redirect("/")
            return "Невірний пароль"


    return render_template(template_name_or_list='log.html', body=data_dict, is_auth = current_user.is_authenticated, login_meneger = login_manager)

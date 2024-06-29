import flask
import os 
import json
from flask_login import current_user
def render_home():
    path_json = os.path.abspath(__file__ + "/../../static/home_page/json/data.json")
    with open(path_json, "r", encoding="utf-8") as file:
        data_dict = json.load(file)
    
    print(current_user.is_authenticated)
    if current_user.is_authenticated:
        print(current_user.is_authenticated,)
        return flask.render_template(
            template_name_or_list="home.html",
            body = data_dict,
            is_authenticated = current_user.is_authenticated,
            user_name = current_user.name,
            is_admin = current_user.is_admin
        )

    return flask.render_template(template_name_or_list= "home.html", body = data_dict )

    
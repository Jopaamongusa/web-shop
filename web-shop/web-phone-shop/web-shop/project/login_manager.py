import flask_login 

from .settings import project
from reg_page.models import Users

project.secret_key = '200'

login_manager = flask_login.LoginManager(project)

@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)
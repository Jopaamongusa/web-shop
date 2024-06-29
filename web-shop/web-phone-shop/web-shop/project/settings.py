import flask
import flask_sqlalchemy
import flask_migrate
import os

project = flask.Flask(
    import_name="settings",
    template_folder= "project/templates",
    instance_path= os.path.abspath(__file__ + "/.."),
)

project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

DATABASE = flask_sqlalchemy.SQLAlchemy(app = project)

migrate = flask_migrate.Migrate(app = project, db= DATABASE)

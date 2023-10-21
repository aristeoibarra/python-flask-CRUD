from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging

app = Flask(__name__)
app.config.from_object(Config)

if app.config["ENV"] == "development":
    app.config.from_object("config.DevelopmentConfig")
elif app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")

logging.basicConfig(
    filename=app.config["LOG_FILENAME"],
    level=app.config["LOG_LEVEL"],
    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
    datefmt="%d/%m/%Y %I:%M:%S %p",
    filemode="a",
    encoding="utf-8",
)


class Base(object):
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate()
login_manager = LoginManager()

login_manager.login_view = "user_controller.login"
login_manager.session_protection = "strong"

app.config["SQLALCHEMY_DATABASE_URI"] = app.config["SQLALCHEMY_DATABASE_URI"]
app.secret_key = app.config["SECRET_KEY"]

db.init_app(app)
migrate.init_app(app, db)

login_manager.init_app(app)


from app.models import User
from app.controllers import user_controller
from app.controllers import home_controller
from app.controllers import main_controller
from app.controllers import product_controller

app.register_blueprint(user_controller)
app.register_blueprint(home_controller)
app.register_blueprint(main_controller)
app.register_blueprint(product_controller)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from flask import Blueprint, redirect, url_for
from flask_login import current_user

main_controller = Blueprint("main_controller", __name__)


@main_controller.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("home_controller.home"))
    else:
        return redirect(url_for("user_controller.login"))

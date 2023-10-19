from flask import Blueprint, render_template
from flask_login import login_required

home_controller = Blueprint("home_controller", __name__)


@home_controller.route("/home")
@login_required
def home():
    return render_template("home.html", key="home")

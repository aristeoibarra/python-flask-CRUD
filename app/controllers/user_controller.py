from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from app import db
from app.models import User
from app.forms import RegistrationForm
from app.forms import LoginForm

user_controller = Blueprint("user_controller", __name__)


@user_controller.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(user_email=email).first()

        if user and check_password_hash(user.user_password, password):
            login_user(user)
            return redirect(url_for("home_controller.home"))
        else:
            flash("Invalid email/password combination")
            return redirect(url_for("user_controller.login"))

    return (
        current_user.is_authenticated
        and redirect(url_for("home_controller.home"))
        or render_template("login.html", form=form)
    )


@user_controller.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("user_controller.login"))


@user_controller.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        name = form.name.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(user_email=email).first()

        if user:
            flash("Email address already exists")
            form.email.errors.append("Email address already exists")
        else:
            new_user = User(
                user_name=name,
                user_lastname=lastname,
                user_email=email,
                user_password=password,
            )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("user_controller.login"))

    return (
        current_user.is_authenticated
        and redirect(url_for("home_controller.home"))
        or render_template("register.html", form=form)
    )

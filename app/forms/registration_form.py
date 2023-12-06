from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegistrationForm(FlaskForm):
    name = StringField("Username", validators=[DataRequired(), Length(min=2, max=64)])
    lastname = StringField(
        "Lastname", validators=[DataRequired(), Length(min=2, max=64)]
    )
    email = StringField(
        "Email", validators=[DataRequired(), Email(), Length(min=6, max=35)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=3, max=20)]
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )

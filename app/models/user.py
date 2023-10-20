from app import db
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64))
    user_lastname = db.Column(db.String(64))
    user_email = db.Column(db.String(120), unique=True)
    user_password = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, user_name, user_lastname, user_email, user_password):
        self.user_name = user_name
        self.user_lastname = user_lastname
        self.user_email = user_email
        self.user_password = generate_password_hash(user_password)

    def set_password(self, password):
        self.user_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.user_password, password)

    def is_active(self):
        return self.is_active

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user_id

    def is_authenticated(self):
        return True

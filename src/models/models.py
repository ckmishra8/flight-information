from datetime import datetime

from flask import g

from src.conf.auth import auth, jwt
from src import logger
from src.database.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=80), unique=True)
    password = db.Column(db.String(length=80))
    email = db.Column(db.String(length=80), unique=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    user_role = db.Column(db.String, default="user")

    def generate_auth_token(self, permission_level):
        if permission_level == 1:
            token = jwt.dumps({"email": self.email, "admin": 1})
            return token
        elif permission_level == 2:
            token = jwt.dumps({"email": self.email, "admin": 2})
            return token
        return jwt.dumps({"email": self.email, "admin": 0})

    @staticmethod
    @auth.verify_token
    def verify_auth_token(token):
        g.user = None
        try:
            data = jwt.loads(token)
        except Exception as e:
            logger.exception(e)
            return False
        if "email" and "admin" in data:
            g.user = data["email"]
            g.admin = data["admin"]
            return True
        return False


class Blacklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(length=255))


class Flight(db.Model):
    flight_number = db.Column(db.Integer, primary_key=True)
    flight_name = db.Column(db.String(length=80), nullable=False)
    scheduled_date = db.Column(db.String(length=10), nullable=False)
    scheduled_time = db.Column(db.String(length=10), nullable=False)
    expected_arrival_date = db.Column(db.String(length=10), nullable=False)
    expected_arrival_time = db.Column(db.String(length=10), nullable=False)
    departure = db.Column(db.String(length=80), nullable=False)
    destination = db.Column(db.String(length=80), nullable=False)
    fare_in_usd = db.Column(db.Integer, nullable=False)
    flight_duration = db.Column(db.String(length=10), nullable=False)

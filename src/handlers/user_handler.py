from flask import request
from flask_restful import Resource

import src.error.errors as error
from src import logger
from src.conf.auth import auth
from src.database.database import db
from src.models.models import User, Blacklist


class Index(Resource):
    @staticmethod
    def get():
        return {"status": "Flight information APIs"}


class Register(Resource):
    @staticmethod
    def post():
        try:
            username, password, email = (
                request.json.get("username").strip(),
                request.json.get("password").strip(),
                request.json.get("email").strip(),
            )
        except Exception as e:
            logger.info(f"Credentials or email is wrong. {str(e)}")
            return error.INVALID_INPUT
        if username is None or password is None or email is None:
            return error.INVALID_INPUT
        user = User.query.filter_by(email=email).first()
        if user is not None:
            return error.ALREADY_EXIST
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        return {"status": "registration completed."}


class Login(Resource):
    @staticmethod
    def post():
        try:
            email, password = (
                request.json.get("email").strip(),
                request.json.get("password").strip(),
            )
        except Exception as e:
            logger.info(f"Email or password is wrong. {str(e)}")
            return error.INVALID_INPUT
        if email is None or password is None:
            return error.INVALID_INPUT
        user = User.query.filter_by(email=email, password=password).first()
        if user is None:
            return error.UNAUTHORIZED
        return {"token": user.generate_auth_token(0).decode()}


class Logout(Resource):
    @staticmethod
    @auth.login_required
    def post():
        token = dict(request.headers)['Authorization'].split(' ')[1]
        ref = Blacklist.query.filter_by(token=token).first()
        if ref:
            logger.info("Token already expired.")
            return {"status": "Already logged out."}
        db.session.add(Blacklist(token=token))
        db.session.commit()
        return {"status": "Logged out."}

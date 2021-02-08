from flask_testing import TestCase

from main import create_app
from src.conf.auth import jwt
from src.database.database import db
from src.handlers.user_handler import User


class LoginTest(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        return create_app()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_login(self):
        User.query.filter_by(email="test").first()
        user = User(
            username="test",
            password="test",
            email="test@test.com",
        )
        db.session.add(user)
        db.session.commit()

        data = {"email": "test@test.com", "password": "test"}
        response = self.client.post("/v1/auth/login", json=data)
        self.assert200(response)
        tokenized_data = jwt.loads(response.json.get("token"))
        self.assertEquals(tokenized_data.get("email"), user.email)

    def test_login_missing_parameter(self):
        User.query.filter_by(email="test").first()
        user = User(
            username="test",
            password="test",
            email="test@test.com",
        )
        db.session.add(user)
        db.session.commit()

        expected_result = {"message": "Invalid input."}
        data = {"email": "test@test.com"}
        response = self.client.post("/v1/auth/login", json=data)
        self.assertEquals(expected_result, response.json)

    def test_login_none_parameter(self):
        User.query.filter_by(email="test").first()
        user = User(
            username="test",
            password="test",
            email="test@test.com",
        )
        db.session.add(user)
        db.session.commit()

        expected_result = {"message": "Invalid input."}
        data = {"email": "test@test.com", "password": None}
        response = self.client.post("/v1/auth/login", json=data)
        self.assertEquals(expected_result, response.json)

    def test_login_doesnt_exist(self):
        expected_result = {'message': 'Wrong credentials.'}
        data = {"email": "invalid@test.com", "password": "password"}
        response = self.client.post("/v1/auth/login", json=data)
        assert expected_result == response.json

    def test_login_wrong_password(self):
        expected_result = {"message": "Wrong credentials."}
        User.query.filter_by(email="test").first()
        user = User(
            username="test",
            password="test",
            email="test@test.com",
        )
        db.session.add(user)
        db.session.commit()

        data = {"email": "test@test.com", "password": "invalid"}
        response = self.client.post("/v1/auth/login", json=data)
        self.assertEquals(expected_result, response.json)

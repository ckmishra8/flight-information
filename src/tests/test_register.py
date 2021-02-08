from flask_testing import TestCase

from main import create_app
from src.database.database import db
from src.handlers.user_handler import User


class RegisterTest(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        return create_app()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register(self):
        data = {
            "email": "test@test.com",
            "password": "test",
            "username": "test"
        }
        expected = {'status': 'registration completed.'}
        response = self.client.post("/v1/auth/register", json=data)
        self.assertEquals(expected, response.json)

    def test_user_already_registered(self):
        User.query.filter_by(email="test").first()
        user = User(
            username="test",
            password="test",
            email="test@test.com",
        )
        db.session.add(user)
        db.session.commit()

        data = {
            "email": "test@test.com",
            "password": "test",
            "username": "test"
        }
        expected = {'message': 'Already exists.'}
        response = self.client.post("/v1/auth/register", json=data)
        self.assertEquals(expected, response.json)

    def test_invalid_registration(self):
        data = {
            "email": "test@test.com",
            "username": "test"
        }
        expected = {'message': 'Invalid input.'}
        response = self.client.post("/v1/auth/register", json=data)
        self.assertEquals(expected, response.json)

from flask_testing import TestCase

from src.database.database import db
from main import create_app


class IndexTest(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        return create_app()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        expected_result = {'status': 'Flight information APIs'}
        response = self.client.get("/")
        self.assert200(response)
        self.assertEquals(expected_result, response.json)

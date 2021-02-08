from flask_testing import TestCase

from main import create_app
from src.database.database import db


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

    def test_update_flight(self):
        data = {
            "email": "test@test.com",
            "password": "test",
            "username": "test"
        }

        self.client.post("/v1/auth/register", json=data)
        data = {"email": "test@test.com", "password": "test"}
        response = self.client.post("/v1/auth/login", json=data)
        data = {
            "flight_number": 6,
            "flight_name": "Air Asia",
            "departure": "BLR",
            "destination": "XLR",
            "fare_in_usd": 200,
            "scheduled_date": "02/08/2021",
            "scheduled_time": "02:21:24",
            "expected_arrival_date": "02/09/2021",
            "expected_arrival_time": "03:40:24"
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {response.json['token']}"
        }
        self.client.post("/v1/flight/add", json=data, headers=headers)
        data = {
            "flight_number": 6,
            "flight_name": "Air Asia",
            "departure": "BLR",
            "destination": "XLR",
            "fare_in_usd": 200,
            "scheduled_date": "02/08/2021",
            "scheduled_time": "02:21:24",
            "expected_arrival_date": "02/09/2021",
            "expected_arrival_time": "03:40:24"
        }
        response = self.client.post("/v1/flight/update", json=data,
                                    headers=headers)
        expected = {'status': 'Flight details updated.'}
        self.assertEquals(expected, response.json)
        self.assert200(response)

    def test_update_removed_flight_details(self):
        data = {
            "email": "test@test.com",
            "password": "test",
            "username": "test"
        }

        self.client.post("/v1/auth/register", json=data)
        data = {"email": "test@test.com", "password": "test"}
        response = self.client.post("/v1/auth/login", json=data)
        data = {
            "flight_number": 6,
            "flight_name": "Air Asia",
            "departure": "BLR",
            "destination": "XLR",
            "fare_in_usd": 200,
            "scheduled_date": "02/08/2021",
            "scheduled_time": "02:21:24",
            "expected_arrival_date": "02/09/2021",
            "expected_arrival_time": "03:40:24"
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {response.json['token']}"
        }
        self.client.post("/v1/flight/add", json=data, headers=headers)
        self.client.post("/v1/flight/remove", json=data,
                         headers=headers)
        data = {
            "flight_number": 6,
            "flight_name": "Air India",
            "departure": "PTL",
            "destination": "QRT",
            "fare_in_usd": 300
        }
        response = self.client.post("/v1/flight/update", json=data,
                                    headers=headers)
        expected = {'status': 'Flight details updated.'}
        self.assertEquals(expected, response.json)
        self.assert200(response)

    def test_invalid_token_update_flight(self):
        data = {
            "email": "test@test.com",
            "password": "test",
            "username": "test"
        }

        self.client.post("/v1/auth/register", json=data)
        data = {"email": "test@test.com", "password": "test"}
        response = self.client.post("/v1/auth/login", json=data)
        data = {
            "flight_number": 6,
            "flight_name": "Air Asia",
            "departure": "BLR",
            "destination": "XLR",
            "fare_in_usd": 200,
            "scheduled_date": "02/08/2021",
            "scheduled_time": "02:21:24",
            "expected_arrival_date": "02/09/2021",
            "expected_arrival_time": "03:40:24"
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {response.json['token']}"
        }
        self.client.post("/v1/flight/add", json=data, headers=headers)
        headers = {
            "Content-Type": "application/json",
            "Authorization": "InvalidToken"
        }
        response = self.client.post("/v1/flight/update", json=data,
                                    headers=headers)
        self.assert401(response)

    def test_update_flight_after_logout(self):
        data = {
            "email": "test@test.com",
            "password": "test",
            "username": "test"
        }

        self.client.post("/v1/auth/register", json=data)
        data = {"email": "test@test.com", "password": "test"}
        response = self.client.post("/v1/auth/login", json=data)
        data = {
            "flight_number": 6,
            "flight_name": "Air Asia",
            "departure": "BLR",
            "destination": "XLR",
            "fare_in_usd": 200,
            "scheduled_date": "02/08/2021",
            "scheduled_time": "02:21:24",
            "expected_arrival_date": "02/09/2021",
            "expected_arrival_time": "03:40:24"
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {response.json['token']}"
        }
        self.client.post("/v1/flight/add", json=data, headers=headers)
        data = {
            "flight_number": 6,
            "flight_name": "Air India",
            "departure": "PTL",
            "destination": "QRT",
            "fare_in_usd": 300
        }
        response = self.client.post("/v1/flight/update", json=data,
                                    headers=headers)
        expected = {'status': 'Flight details updated.'}
        self.assertEquals(expected, response.json)
        self.assert200(response)
        response = self.client.post("/v1/auth/logout", headers=headers)
        self.assert200(response)
        self.assertEquals({"status": "Logged out."}, response.json)
        response = self.client.post("/v1/flight/update", json=data,
                                    headers=headers)
        self.assert401(response)
        self.assertEquals({'message': 'Wrong credentials.'},
                          response.json)

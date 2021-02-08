from datetime import datetime
from json import dumps, loads

from flask import request
from flask_restful import Resource

import src.error.errors as error
from src.conf.auth import auth
from src.database.database import db
from src.models.models import Flight, Blacklist


class AddFlightInformation(Resource):
    @staticmethod
    @auth.login_required
    def post():
        token = dict(request.headers)['Authorization'].split(' ')[1]
        query = db.session.query(Blacklist).filter_by(token=token)
        tokens = db.session.execute(query).fetchall()
        if len(tokens):
            return error.UNAUTHORIZED
        sc_date = datetime.utcnow().strftime("%m/%d/%Y")
        sc_time = datetime.utcnow().strftime("%H:%M:%S")
        ex_date = datetime.utcnow().strftime("%m/%d/%Y")
        ex_time = datetime.utcnow().strftime("%H:%M:%S")
        sc_date = request.json["scheduled_date"].strip() if \
            request.json.get("scheduled_date") else sc_date
        sc_time = request.json["scheduled_time"].strip() if \
            request.json.get("scheduled_time") else sc_time
        ex_date = request.json["expected_arrival_date"].strip() if \
            request.json.get("expected_arrival_date") else ex_date
        ex_time = request.json["expected_arrival_time"].strip() if \
            request.json.get("expected_arrival_time") else ex_time
        sc_timestamp = datetime.strptime(
            sc_date + ' ' + sc_time, '%m/%d/%Y %H:%M:%S')
        ex_timestamp = datetime.strptime(
            ex_date + ' ' + ex_time, '%m/%d/%Y %H:%M:%S')
        duration = (ex_timestamp - sc_timestamp).total_seconds() / 3600
        try:
            flight_number, flight_name, departure, destination, \
                fare_in_usd = \
                (
                    request.json.get("flight_number"),
                    request.json.get("flight_name").strip(),
                    request.json.get("departure").strip(),
                    request.json.get("destination").strip(),
                    request.json.get("fare_in_usd")
                )
        except AttributeError:
            return error.INVALID_INPUT
        flight = Flight(
            flight_number=flight_number, flight_name=flight_name,
            departure=departure, destination=destination,
            fare_in_usd=fare_in_usd, scheduled_date=sc_date,
            scheduled_time=sc_time, expected_arrival_date=ex_date,
            expected_arrival_time=ex_time,
            flight_duration=f"{round(duration)}{' hours'}"
        )
        details = Flight.query.filter_by(
            flight_number=flight_number).first()
        if details is not None:
            return error.ALREADY_EXIST
        db.session.add(flight)
        db.session.commit()
        return {"status": "Flight details recorded."}


class RemoveFlightInformation(Resource):
    @staticmethod
    @auth.login_required
    def post():
        token = dict(request.headers)['Authorization'].split(' ')[1]
        query = db.session.query(Blacklist).filter_by(token=token)
        tokens = db.session.execute(query).fetchall()
        if len(tokens):
            return error.UNAUTHORIZED
        try:
            flight_number = request.json.get("flight_number")
        except AttributeError:
            return error.INVALID_INPUT
        details = Flight.query.filter_by(
            flight_number=flight_number).delete()
        if not details:
            return error.DOES_NOT_EXIST
        db.session.commit()
        return {"status": "Flight details removed."}


class UpdateFlightInformation(Resource):
    @staticmethod
    @auth.login_required
    def post():
        token = dict(request.headers)['Authorization'].split(' ')[1]
        query = db.session.query(Blacklist).filter_by(token=token)
        tokens = db.session.execute(query).fetchall()
        if len(tokens):
            return error.UNAUTHORIZED
        if not request.json.get("flight_number"):
            return error.DOES_NOT_EXIST
        Flight.query.filter_by(
            flight_number=request.json.get("flight_number")
        ).update(request.json)
        db.session.commit()
        return {"status": "Flight details updated."}


class SearchFlightInformation(Resource):
    @staticmethod
    @auth.login_required
    def get():
        token = dict(request.headers)['Authorization'].split(' ')[1]
        query = db.session.query(Blacklist).filter_by(token=token)
        tokens = db.session.execute(query).fetchall()
        if len(tokens):
            return error.UNAUTHORIZED
        query = db.session.query(Flight).filter_by(**request.json)
        rows = db.session.execute(query).fetchall()
        return error.DOES_NOT_EXIST if not rows else loads(dumps([(
            dict(row.items())) for row in rows]))

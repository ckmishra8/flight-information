from flask_restful import Api

from src.handlers.flight_handler import AddFlightInformation, \
    RemoveFlightInformation, UpdateFlightInformation, \
    SearchFlightInformation
from src.handlers.user_handler import Index, Login, Logout, Register


def generate_routes(app):
    api = Api(app)
    api.add_resource(Index, "/")
    api.add_resource(Register, "/v1/auth/register")
    api.add_resource(Login, "/v1/auth/login")
    api.add_resource(Logout, "/v1/auth/logout")
    api.add_resource(AddFlightInformation, "/v1/flight/add")
    api.add_resource(RemoveFlightInformation, "/v1/flight/remove")
    api.add_resource(UpdateFlightInformation, "/v1/flight/update")
    api.add_resource(SearchFlightInformation, "/v1/flight/search")

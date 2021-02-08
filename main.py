import os

from flask import Flask

from src.conf.config import SQLALCHEMY_DATABASE_URI
from src.conf.routes import generate_routes
from src.database.database import db


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    generate_routes(app)
    db.init_app(app)
    if not os.path.exists(SQLALCHEMY_DATABASE_URI):
        db.app = app
        db.create_all()
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, host='localhost', use_reloader=True)

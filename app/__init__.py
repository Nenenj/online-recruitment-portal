#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../instance/config.py')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app import routes, models
    return app

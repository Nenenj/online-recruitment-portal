#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Directly set configuration from the env variables
    app.config['SECRET_KEY'] = os.getenv(
            'SECRET_KEY', 'default_secret_key'
            )
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
            'DATABASE_URI',
            'mysql+pymysql://hbnb_dev:hbnb_dev_pwd@mynenenj.tech/'
            'Recruitment_portal'
            )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Debug print statements to check configurations
    print('Config file loaded successfully.')
    print(f"SECRET_KEY: {app.config.get('SECRET_KEY')}")
    print(
        f"SQLALCHEMY_DATABASE_URI: {app.config.get('SQLALCHEMY_DATABASE_URI')}"
        )

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    from app.routes import init_routes
    init_routes(app)

    return app

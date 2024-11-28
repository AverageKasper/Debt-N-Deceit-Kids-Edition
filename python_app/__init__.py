from flask import Flask
from flask_cors import CORS
from python_app.routes import register_blueprints

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register blueprints
    register_blueprints(app)

    return app
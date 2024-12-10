from flask import Flask
from flask_cors import CORS
from python_app.routes import register_blueprints
from python_app.routes.lollipop_task import lollipop_blueprint  # Import the lollipop blueprint

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.secret_key='secret_key'

    # Register blueprints
    register_blueprints(app)
    app.register_blueprint(lollipop_blueprint, url_prefix='/lollipop')  # Register the lollipop blueprint
    return app
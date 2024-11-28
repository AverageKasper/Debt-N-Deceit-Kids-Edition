from python_app.routes.pickpocket import pickpocket_blueprint


def register_blueprints(app):
    app.register_blueprint(pickpocket_blueprint, url_prefix='/pickpocket')

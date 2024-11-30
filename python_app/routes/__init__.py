from python_app.routes.small_task import small_blueprint
from python_app.routes.start import start_blueprint
from python_app.routes.task import task_blueprint
from python_app.routes.sql import sql_blueprint
from python_app.routes.random_events import random_blueprint
from python_app.routes.medium_task import medium_blueprint


def register_blueprints(app):
    app.register_blueprint(small_blueprint, url_prefix='/small')
    app.register_blueprint(start_blueprint, url_prefix='/start')
    app.register_blueprint(task_blueprint, url_prefix='/task')
    app.register_blueprint(sql_blueprint, url_prefix='/sql')
    app.register_blueprint(random_blueprint, url_prefix='/random')
    app.register_blueprint(medium_blueprint, url_prefix='/medium')

from python_app.routes.pickpocket import pickpocket_blueprint
from python_app.routes.game_loop import game_loop_blueprint
from python_app.routes.task import task_blueprint
from python_app.routes.sql import sql_blueprint


def register_blueprints(app):
    app.register_blueprint(pickpocket_blueprint, url_prefix='/pickpocket')
    app.register_blueprint(game_loop_blueprint, url_prefix='/game_loop')
    app.register_blueprint(task_blueprint, url_prefix='/task')
    app.register_blueprint(sql_blueprint, url_prefix='/sql')

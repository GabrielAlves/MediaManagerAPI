from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config = None):
    app = Flask(__name__)

    if test_config:
        app.config.update(test_config)

    else:
        from .config import Config
        app.config.from_object(Config)

    from . import routes
    app.register_blueprint(routes.bp)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
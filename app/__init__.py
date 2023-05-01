from flask import Flask
from flask_jwt_extended import JWTManager
from flask_login import current_user, LoginManager

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    from .main import bp as main_bp
    app.register_blueprint(main_bp)
    from . import models
    from .fake_data import bp as fake_bp
    app.register_blueprint(fake_bp)
    from .user import bp as user_bp
    app.register_blueprint(user_bp)
    from .post import bp as post_bp
    app.register_blueprint(post_bp)
    from .api import bp as api_bp
    app.register_blueprint(api_bp)
    login_manager.init_app(app)
    jwt.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return models.User.query.get(user_id)

    @app.context_processor
    def context_processor():
        return dict(
            current_user=current_user
        )

    return app


app = create_app()

from flask import Flask
from flask_login import current_user
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    from .main import bp as main_bp
    app.register_blueprint(main_bp)
    from .models import User  # noqa
    from .fake_data import bp as fake_bp
    app.register_blueprint(fake_bp)

    @app.context_processor
    def context_processor():
        return dict(
            current_user=current_user
        )

    return app


app = create_app()

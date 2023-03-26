from flask import Flask
from flask_login import current_user
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    from .main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.context_processor
    def context_processor():
        return dict(
            current_user=current_user
        )
    return app


app = create_app()

from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='auth')


@bp.route('/')
def index():
    return 'It is auth!'

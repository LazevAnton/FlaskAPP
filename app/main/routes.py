from app.main import bp


@bp.route('/')
def index():
    return 'It is auth!'

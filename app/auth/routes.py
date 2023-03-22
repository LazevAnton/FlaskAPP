from app.auth import bp


@bp.route('/')
def index():
    return 'It is auth!'

#
# @bp.login('/login')
# def login():
#     pass

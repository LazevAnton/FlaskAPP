from app.main import bp
from flask import render_template


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='FlaskAPP')


@bp.route('/about')
def about():
    return render_template('about.html', title='About')

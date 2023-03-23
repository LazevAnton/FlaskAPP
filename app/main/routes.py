from app.main import bp
from flask import render_template


@bp.route('/about')
def index():
    return render_template('about.html', title='About')

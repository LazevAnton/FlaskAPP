from pathlib import Path

from flask import Blueprint
from sqlalchemy import func

import config
from .. import db
from ..models import User, Profile
import pandas as pd

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.cli.command('extract_users')
def extract_users():
    user_data = []
    users_info = db.session.query(User).all()
    for user in users_info:
        user_data.append(
            {
                'UserName': user.username,
                'Email': user.email,
                'FullName': user.profile.fullname,
                'PostCount': user.posts.count()
            }
        )
    df = pd.DataFrame(user_data, columns=['UserName', 'Email', 'FullName', 'PostCount'])
    df.to_csv(Path(config.Config.basedir)/ 'users.csv')
from . import routes  # noqa

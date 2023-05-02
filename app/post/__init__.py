from pathlib import Path

import click
from flask import Blueprint
import pandas as pd

import config
from .. import db
from ..models import Post, User

bp = Blueprint('post', __name__, url_prefix='/post')


@bp.cli.command('extract_posts')
@click.argument('user_id', type=int)
def extract_posts(user_id):
    post_info = []
    user_name = db.session.query(User.username).filter(User.id == user_id).scalar()
    if user_name:
        posts = db.session.query(Post).filter(Post.author_id == user_id).all()
        for post in posts:
            title = post.title
            likes = len(post.likes)
            dislikes = len(post.dislikes)
            created = post.created_at
            post_info.append(
                {
                    'PostTitle': title,
                    'Likes': likes,
                    'Dislikes': dislikes,
                    'CreatedAT': created
                }
            )
        df = pd.DataFrame(post_info, columns=['PostTitle', 'Likes', 'Dislikes', 'CreatedAT'])
        df.to_csv(Path(config.Config.BASEDIR) / f'{user_name}_posts_info.csv')
    else:
        print('Error! User didnt found')


from . import routes  # noqa

from flask_restful import Resource
from app import db
from app.models import Post
from flask import jsonify

from app.schemas import PostSchema


class PostUserResource(Resource):
    def get(self, user_id):
        user_post = db.session.query(Post).filter(Post.author_id == user_id).all()
        return jsonify(PostSchema().dump(user_post, many=True))
    # def get(self):
    #     posts = db.session.query(Post, User.username).join(User).all()
    #     post_list = []
    #     for post, username in posts:
    #         post_dict = {
    #             'author': username,
    #             'title': post.title,
    #             'content': post.content,
    #             'created_at': post.created_at.isoformat(),
    #             'likes': post.dislikes,
    #             'dislike': post.likes
    #
    #
    #         }
    #         post_list.append(post_dict)
    #     return jsonify(post_list)

from flask_restful import Resource
from app import db
from app.models import Post
from flask import jsonify, request
from app.schemas import PostSchema
from app.service import PostService

post_service = PostService()


class PostsResource(Resource):
    def get(self):
        posts = db.session.query(Post).all()
        return jsonify(PostSchema().dump(posts, many=True))

    #     user_post = db.session.query(Post).filter(Post.author_id == user_id).all()
    #     return jsonify(PostSchema().dump(user_post, many=True))
    def post(self):
        json_data = request.get_json()
        post = post_service.create(**json_data)
        return jsonify(PostSchema().dump(post, many=False))


class PostResource(Resource):
    def get(self, post_id):
        post = post_service.get_by_id(post_id)
        return jsonify(PostSchema().dump(post, many=False))

from flask import jsonify, request
from flask_restful import Resource
from app import db
from app.models import Like
from app.schemas import LikeSchema
from app.service import LikeService

like_service = LikeService()


class LikesResource(Resource):
    def get(self):
        likes = db.session.query(Like).all()
        return jsonify(LikeSchema().dump(likes, many=True))

    def post(self):
        pass


class LikeResource(Resource):
    def get(self, post_id):
        like = like_service.get_by_post_id(post_id)
        post_data = LikeSchema().dump(like, many=False)
        post_data['likes:'] = like
        return jsonify(post_data)


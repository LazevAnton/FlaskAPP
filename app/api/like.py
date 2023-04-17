from flask import jsonify
from flask_restful import Resource
from app import db
from app.models import Like
from app.schemas import LikeSchema


class LikesResource(Resource):
    def get(self):
        likes = db.session.query(Like).all()
        return jsonify(LikeSchema().dump(likes, many=True))

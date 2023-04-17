from flask import jsonify
from flask_restful import Resource

from app import db
from app.models import Dislike
from app.schemas import DisLikeSchema


class DisLikesResource(Resource):
    def get(self):
        dislikes = db.session.query(Dislike).all()
        return jsonify(DisLikeSchema().dump(dislikes, many=True))
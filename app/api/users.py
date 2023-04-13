from flask_restful import Resource
from flask import jsonify
from app.models import User
from app.schemas import UserSchema
from app import db


class UsersResource(Resource):
    def get(self):
        users = db.session.query(User).all()
        return jsonify(UserSchema(exclude=('password', 'id',)).dump(users, many=True))

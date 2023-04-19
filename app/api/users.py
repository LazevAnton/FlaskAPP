from flask_restful import Resource
from flask import jsonify, request
from app.models import User
from app.schemas import UserSchema
from app import db
from app.service import UserService

user_service = UserService()


class UsersResource(Resource):
    def get(self):
        users = db.session.query(User).all()
        return jsonify(UserSchema(exclude=('password', 'id',)).dump(users, many=True))

    def post(self):
        json_data = request.get_json()
        user = user_service.create(**json_data)
        return jsonify(UserSchema().dump(user, many=False))


class UserResource(Resource):
    def get(self, user_id):
        user = user_service.get_by_id(user_id)
        return jsonify(UserSchema(exclude=('password',)).dump(user, many=False))

    def put(self, user_id):
        json_data = request.get_json()
        json_data['id'] = user_id
        update_user = user_service.update(json_data)
        return jsonify(UserSchema().dump(update_user, many=False))

    def delete(self, user_id):
        user = user_service.delete(user_id)
        return jsonify(UserSchema().dump(user, many=False))

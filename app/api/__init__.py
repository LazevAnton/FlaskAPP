from flask import Blueprint
from flask_restful import Api

from .dislike import DisLikesResource
from .like import LikesResource
from .users import UsersResource, UserResource
from .posts import PostUserResource

bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(bp)

api.add_resource(UsersResource, '/users', endpoint='users_list')
api.add_resource(UserResource, '/users/<int:user_id>', endpoint='user_details')
api.add_resource(PostUserResource, '/users/<int:user_id>/posts', endpoint='user_posts')
api.add_resource(LikesResource, '/likes', endpoint='likes_list')
api.add_resource(DisLikesResource, '/dislikes', endpoint='dislikes_list')

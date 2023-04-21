from flask import Blueprint
from flask_restful import Api
from .like import LikesResource, LikeResource
from .users import UsersResource, UserResource, UsersPostResource
from .posts import PostsResource, PostResource

bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(bp)

api.add_resource(UsersResource, '/users', endpoint='users_list')
api.add_resource(UserResource, '/users/<int:user_id>', endpoint='user_details')
api.add_resource(UsersPostResource, '/users/<int:user_id>/posts', endpoint='user_post_list')
api.add_resource(UsersPostResource, '/users/<int:user_id>/posts', endpoint='crete_post_user_id')
api.add_resource(UsersPostResource, '/users/<int:user_id>/posts/<int:post_id>', endpoint='user_post_by_post_id')
api.add_resource(PostsResource, '/posts', endpoint='posts_list')
api.add_resource(PostResource, '/posts/<int:post_id>', endpoint='post_details')
api.add_resource(LikesResource, '/likes', endpoint='likes_list')
api.add_resource(LikeResource, '/likes/<int:post_id>', endpoint='like_post_count')

from app import db
from app.models import User, Profile, Post, Like, Dislike
from app.schemas import UserSchema, PostSchema, LikeSchema


class UserService:

    def get_by_id(self, user_id):
        user = db.session.query(User).filter(User.id == user_id).first_or_404()
        return user

    def get_all_user_posts(self, user_id):
        posts = db.session.query(Post).filter(Post.author_id == user_id).all()
        user_posts = []
        for post in posts:
            user_posts.append({
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'created_at': post.created_at
            })
        return user_posts

    def get_by_username(self, username):
        user = db.session.query(User).filter(User.username == username).first_or_404()
        return user

    def create(self, **kwargs):
        user = User(username=kwargs.get('username'), email=kwargs.get('email'))
        user.set_password(kwargs.get('password'))

        db.session.add(user)
        db.session.commit()

        profile = Profile(user_id=user.id)
        db.session.add(profile)
        db.session.commit()

        return user

    def update(self, data):
        user = self.get_by_id(data['id'])
        data['profile']['id'] = user.profile.id
        data['profile']['user_id'] = user.id

        user = UserSchema(exclude=('password',)).load(data)
        db.session.add(user)
        db.session.commit()

        return user

    def delete(self, user_id):
        user = self.get_by_id(user_id)
        profile = user.profile
        db.session.delete(profile)
        db.session.commit()

        db.session.delete(user)
        db.session.commit()

        return True


class PostService:
    def get_by_id(self, post_id):
        post = db.session.query(Post).filter(Post.id == post_id).first_or_404()
        return post

    def get_likes(self, post_id):
        likes = db.session.query(Like).filter(Like.post_id == post_id).count()
        return likes

    def get_dislikes(self, post_id):
        dislikes = db.session.query(Dislike).filter(Dislike.post_id == post_id).count()
        return dislikes

    def create(self, **kwargs):
        post = Post(title=kwargs.get('title'), content=kwargs.get('content'), author_id=kwargs.get('user_id'))
        db.session.add(post)
        db.session.commit()
        return post

    def create_post_by_user_id(self, user_id, **kwargs):
        post = Post(title=kwargs.get('title'), content=kwargs.get('content'), author_id=user_id)
        db.session.add(post)
        db.session.commit()
        return post

    def get_spec_post_by_spec_user(self, user_id, post_id):
        post = db.session.query(Post).filter(Post.id == post_id, Post.author_id == user_id).first()
        return post

    def update(self, post_data):
        post_update = PostSchema().load(post_data)
        db.session.commit()
        return post_update

    def delete(self, post_id):
        post = self.get_by_id(post_id)
        db.session.delete(post)
        db.session.commit()
        return True

    def delete_post_id_by_user_id(self, user_id, post_id):
        post = Post.query.filter(Post.id == post_id, Post.author_id == user_id).first_or_404()
        db.session.delete(post)
        db.session.commit()
        return post


class LikeService:
    def get_by_post_id(self, post_id):
        likes = db.session.query(Like).filter(Like.post_id == post_id)
        return likes.count()

    def create(self, post_id):
        pass

    # def get_dislikes_by_post_id(self, post_id):
    #     dislikes = db.session.query(Dislike).filter(Dislike.post_id == post_id)
    #     return dislikes.count()

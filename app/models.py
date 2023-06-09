from datetime import datetime
from hashlib import md5

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import joinedload

from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)


class User(BaseModel, UserMixin):
    __tablename__ = "user"

    username = db.Column(db.String, unique=True, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    avatar = db.Column(db.String(120), unique=True, nullable=True)

    posts = db.relationship(
        "Post", backref="author", uselist=True, lazy="dynamic", cascade="all,delete"
    )
    likes = db.relationship(
        'Like', backref='user', lazy='dynamic', primaryjoin='User.id==Like.user_id', cascade="all,delete"
    )
    dislikes = db.relationship(
        'Dislike', backref='user', lazy='dynamic', primaryjoin='User.id==Dislike.user_id', cascade="all,delete"
    )

    # list of users that follow you
    followers = db.relationship("Follow", backref="followee", foreign_keys="Follow.followee_id")

    # list of users that you follow
    following = db.relationship("Follow", backref="follower", foreign_keys="Follow.follower_id")

    def avatar(self, size):
        avatar_hash = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{avatar_hash}?d=identicon&s={size}'

    def set_password(self, password):
        """
        Set user password hash
        """
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """
        Check user password hash with existing in db
        """
        return check_password_hash(self.password, password)

    def is_following(self, user):
        """
        Check if the current user is following the given user.
        """
        return Follow.query.filter_by(follower_id=self.id, followee_id=user.id).first() is not None

    def follow(self, user):
        """
        Follow the given user.
        """
        if not self.is_following(user):
            follow = Follow(follower_id=self.id, followee_id=user.id)
            db.session.add(follow)
            db.session.commit()

    def unfollow(self, user):
        """
        Unfollow the given user.
        """
        follow = Follow.query.filter_by(follower_id=self.id, followee_id=user.id).first()
        if follow:
            db.session.delete(follow)
            db.session.commit()

    def get_followers(self):
        """
        Get all followers of the current user.
        """
        following = User.query.join(
            Follow, Follow.followee_id == User.id
        ).filter(
            Follow.follower_id == self.id
        ).options(joinedload(User.followers)).all()
        return following

    def get_following(self):
        """
        Get all users followed by the current user.
        """
        followers = User.query.join(
            Follow, Follow.follower_id == User.id
        ).filter(
            Follow.followee_id == self.id
        ).options(joinedload(User.followers)).all()
        return followers

    def __repr__(self):
        return f"{self.username}"


class Profile(BaseModel):
    __tablename__ = "profiles"
    __table_args__ = (
        db.Index("idx_profiles_user_id", "user_id"),
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id", name="fk_profiles_user_id", ondelete="CASCADE"),
        nullable=False
    )
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    bio = db.Column(db.String)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    facebook_url = db.Column(db.String)
    linkedIn_url = db.Column(db.String)

    user = db.relationship("User", backref=db.backref("profile", uselist=False, lazy='joined'), uselist=False)

    @hybrid_property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'


class Post(BaseModel):
    __tablename__ = 'posts'

    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id", name="fk_posts_author_id", ondelete="CASCADE"),
        nullable=False
    )

    likes = db.relationship("Like", backref="post", uselist=True, cascade="all,delete")
    dislikes = db.relationship("Dislike", backref="post", uselist=True, cascade="all,delete")


# Like model
class Like(BaseModel):
    __tablename__ = "likes"

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', name="fk_likes_user_id"),
        nullable=False
    )
    post_id = db.Column(
        db.Integer,
        db.ForeignKey('posts.id', name="fk_likes_post_id"),
        nullable=False
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Dislike(BaseModel):
    __tablename__ = "dislikes"
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', name="fk_dislikes_user_id"),
        nullable=False
    )
    post_id = db.Column(
        db.Integer,
        db.ForeignKey('posts.id', name="fk_dislikes_post_id"),
        nullable=False
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Follow(db.Model):
    __tablename__ = 'follows'

    follower_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', name="fk_follows_follower_id"),
        primary_key=True
    )
    followee_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', name="fk_follows_followee_id"),
        primary_key=True
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

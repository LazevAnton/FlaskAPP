import click
from app import db
from flask import Blueprint
from faker import Faker
from app.models import User

bp = Blueprint('fake', __name__)
faker = Faker()


@bp.cli.command("create_fake_users")
@click.argument('num', type=int)
def create_fake_users(num):
    users = []
    for u in range(num):
        username = faker.user_name()
        email = faker.email()
        password = faker.password()
        user = (
            db.session.query(User).filter(
                User.username == username,
                User.email == email
            )
        ).first()
        if not user:
            user = User(
                username=username,
                email=email,
                password=password
            )
            db.session.add(user)
            users.append(user)
    db.session.commit()
    print(num, 'users added. ')

import click
from app import db
from flask import Blueprint
from faker import Faker
from app.models import User, Profile

bp = Blueprint('fake', __name__)
faker = Faker()


@bp.cli.command("create_fake_users")
@click.argument('num', type=int)
def create_fake_users(num):
    '''
    one user for test is
    username = ronald67
    passwd = O0#zCQsl@8
    '''
    users = []
    for u in range(num):
        username = faker.user_name()
        email = faker.email(domain='gmail.com')
        passwd = faker.password()
        print(username)
        print(passwd)
        first_name = faker.first_name()
        last_name = faker.last_name()
        facebook_link = f'https://facebook.com/{first_name}.{last_name}'
        linkedin_link = f'https://www.linkedin.com/in/{username}'
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
                password=passwd
            )
            user.set_password(passwd)
            db.session.add(user)
            users.append(user)
            db.session.commit()
            profile = Profile(
                user_id=user.id,
                first_name=first_name,
                last_name=last_name,
                facebook_url=facebook_link,
                linkedIn_url=linkedin_link
            )
            db.session.add(profile)
    db.session.commit()
    print(num, 'users added. ')

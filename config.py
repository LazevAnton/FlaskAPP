from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = 'somestrongpasswd'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///FlaskAPP.db'

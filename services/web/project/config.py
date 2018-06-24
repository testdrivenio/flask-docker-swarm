import os

USER = os.environ.get('DB_USER')
PASSWORD = os.environ.get('DB_PASSWORD')


class ProductionConfig():
    """Production configuration"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'postgres://{USER}:{PASSWORD}@db:5432/users'

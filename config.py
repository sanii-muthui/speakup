import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mannuh:123@localhost/pitch'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

    

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sanii:2125@localhost/pitches'


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sanii:2125@localhost/pitches'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bs string'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    # TODO: A bunch of stuff

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_DB = ''


class TestingConfig(Config):
    DEBUG = True
    FLASK_DB = ''

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

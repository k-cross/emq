import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # TODO: A bunch of stuff 

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    pass

config = {
        'development' : DevelopmentConfig,
        'testing' : TestingConfig,
        'default' : DevelopmentConfig
}

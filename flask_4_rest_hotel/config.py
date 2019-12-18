import os


class Config:
    SECRET_KEY = 'config_key'
    DEBUG = True


class TestConfig(Config):
    SECRET_KEY = 'test_key'


class ProdConfig(Config):
    SECRET_KEY = 'prod_key'
    DEBUG = False


def run_config():
    get_env = {"TEST": TestConfig,
               "PROD": ProdConfig}
    return get_env.get(os.environ.get('ENV'), Config)

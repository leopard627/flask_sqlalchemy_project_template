class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:MyNewPass@localhost/local_test'

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'sqlite://:memory:'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:MyNewPass@localhost/local_test'

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'sqlite://'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

# app.config.from_object('configmodule.ProductionConfig')

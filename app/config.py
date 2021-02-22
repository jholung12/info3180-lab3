import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sadsfosaifbasbffud'
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.mailtrap.io'
    MAIL_PORT = os.environ.get('MAIL_PORT') or '465'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or '026a4b179b420d'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '3a5a316e152084'

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False

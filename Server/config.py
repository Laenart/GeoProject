from store.db_config import DB_CONNECTION_URL


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = DB_CONNECTION_URL


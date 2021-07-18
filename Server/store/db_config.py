import os

USER = os.environ['POSTGRES_USER']
PASSWORD = os.environ['POSTGRES_PASSWORD']
DB = os.environ['POSTGRES_DB']
HOST = os.environ['POSTGRES_HOST']
PORT = os.environ['POSTGRES_PORT']



DB_CONNECTION_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"


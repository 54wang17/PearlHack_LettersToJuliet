import os
DATABASE = 'LettersToJuliet.db'
BASE_PATH = os.path.abspath(os.path.dirname(__file__))
CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

# defines the full path for the database
DATABASE_PATH = os.path.join(BASE_PATH, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
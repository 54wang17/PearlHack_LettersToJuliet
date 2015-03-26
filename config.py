import os
DATABASE = 'LettersToJuliet.db'
BASE_PATH = r'/Users/yiqiwang/Documents/UNC/2015_Spring/PearlHack/PearlHack_LettersToJuliet/'

CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

# defines the full path for the database
DATABASE_PATH = os.path.join(BASE_PATH, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
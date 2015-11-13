# db_create.py


from views import db
from models import User,LetterToJuliet,Reply

# create the database and the db table
db.create_all()

# commit the changes
db.session.commit()
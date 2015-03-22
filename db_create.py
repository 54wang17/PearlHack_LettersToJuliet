# db_create.py


from views import db
from models import User
# from datetime import date

# create the database and the db table
db.create_all()

# insert data
db.session.add(User("wang17", "wangyiqi@gmail.com", "74594w17"))
# db.session.add(Letter("Finish Real Python", date(2014, 3, 13), 10, 1))

# commit the changes
db.session.commit()
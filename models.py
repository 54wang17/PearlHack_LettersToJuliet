from views import db


class User(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
# letters = db.relationship('Letter', backref='poster')

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password


    def __repr__(self):
        return '<User %r>' % (self.name)


class LetterToJuliet(db.Model):
    __tablename__ = 'letter_content'

    id = db.Column(db.Integer, primary_key=True)
    # need foreign key to connect to user
    from_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    title = db.Column(db.String, nullable=False)
    sent_date = db.Column(db.Date, nullable=False)
    content = db.Column(db.Text, nullable=False)
    # 0 means no_reply, 1 means reply.
    reply_status = db.Column(db.Integer, nullable=False)
    
    def __init__(self, from_id, title, content, sent_date, reply_id = None, reply_status=0):
        self.from_id = from_id
        self.title = title
        self.content = content
        self.sent_date = sent_date
        self.reply_status = reply_status
        

    def __repr__(self):
        return '<letter %r>' % (self.title)


class Reply(db.Model):
    __tablename__ = 'reply_content'

    id = db.Column(db.Integer, primary_key=True)
    letter_id = db.Column(db.Integer, db.ForeignKey('letter_content.id'))
    reply_from_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    title = db.Column(db.String, nullable=False)
    reply_date = db.Column(db.Date, nullable=False)
    reply_content = db.Column(db.Text, nullable=True)
    # 0 means unread, 1 means read.
    read_status = db.Column(db.Integer, nullable=False)

    def __init__(self, reply_from_id, title, reply_content, reply_date, letter_id, read_status=0):
        self.reply_from_id = reply_from_id
        self.title = title
        self.reply_content = reply_content
        self.reply_date = reply_date
        self.read_status = read_status
        self.letter_id = letter_id
        

    def __repr__(self):
        return '<letter %r>' % (self.title)




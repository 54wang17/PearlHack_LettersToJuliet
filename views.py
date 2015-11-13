from flask import Flask, flash, redirect, render_template, request, session, url_for
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from forms import NewLetter, RegisterForm, LoginForm

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from models import LetterToJuliet, User, Reply


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('Please login first. Thanks you')
            return redirect(url_for('login'))

    return wrap


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            u = User.query.filter_by(
                name=request.form['username'],
                password=request.form['password']
            ).first()
            if u is None:
                error = 'Invalid username or password.'
                print error,
                return render_template(
                    "login.html",
                    form=form,
                    error=error
                )
            else:
                session['logged_in'] = True
                session['user_id'] = u.id
                flash('Thanks for coming back!')
                print session['user_id']
                return redirect(url_for('user_page', user_id=u.id))
        else:
            print 
            return render_template(
                "login.html",
                form=form,
                error=error
            )
    if request.method == 'GET':
        return render_template('login.html', form=form)


@app.route('/user/<int:user_id>/mainpage/')
@login_required
def user_page(user_id):
    user_id = session['user_id']
    return render_template('user_mainpage.html',user_id=user_id)


@app.route('/user/<int:user_id>/all_letters/')
@login_required
def browse_all_letters(user_id):
    user_id = session['user_id']
    all_letters = db.session.query(LetterToJuliet).filter_by(from_id=user_id)
    return render_template(
        'browse_letters.html',
        user_id=user_id,
        letters=all_letters
    )

@app.route('/user/<int:user_id>/unread_letters/')
@login_required
def browse_unread_letters(user_id):
    user_id = session['user_id']
    unread_letters = db.session.query(LetterToJuliet).filter_by(from_id=user_id, reply_status=1)
    return render_template(
        'browse_letters.html',
        user_id=user_id,
        letters=unread_letters
    )

@app.route('/user/<int:user_id>/new_letter/', methods=['GET', 'POST'])
@login_required
def new_letter(user_id):
    import datetime
    error = None
    form = NewLetter(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_letter = LetterToJuliet(
                user_id,
                form.title.data,
                form.content.data,
                datetime.date.today()
            )
            db.session.add(new_letter)
            db.session.commit()
            flash('The letter was successfully sent to Juliet...')
            return redirect(url_for('user_page', user_id=user_id))
        else:
            return render_template('new_letter.html', uid=user_id, form=form, error=error)
    if request.method == 'GET':
        return render_template('new_letter.html', uid=user_id, form=form)


@app.route('/letter/<int:letter_id>/')
@login_required
def browse_letter(letter_id):
    letter = db.session.query(LetterToJuliet).filter_by(id=letter_id)
    reply_letter = db.session.query(Reply).filter_by(letter_id=letter_id)
    if reply_letter == None:
        return render_template('display_letter.html', letters=letter,replies = reply_letter)
    return render_template('display_letter.html', letters=letter)

@app.route('/user/<int:user_id>/reply_letter/')
@login_required
def get_letter(user_id):
    from sqlalchemy import and_
    letter = db.session.query(LetterToJuliet).filter(LetterToJuliet.from_id!= user_id,LetterToJuliet.reply_status==0).first()
    if letter == None:
        error = "There is no letter need to reply! Click the envelope to return!"
        return render_template('envolope.html', message = error,user_id=user_id)
    message = "Click the envelope to open letter!"
    return redirect(url_for('reply_letter',user_id=user_id, letter_id=letter.id))


@app.route('/user/<int:user_id>/reply_letter/<int:letter_id>',methods=['GET','POST'])
@login_required
def reply_letter(user_id, letter_id):
    import datetime
    error = None
    letter = db.session.query(LetterToJuliet).filter_by(id=letter_id)
    form = NewLetter(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            letter.first().reply_status = 1
            reply_letter = Reply(
                user_id,
                form.title.data,
                form.content.data,
                datetime.date.today(),
                letter_id
                )
            db.session.add(reply_letter)
            db.session.commit()
            flash('The letter was reply')
            return redirect(url_for('user_page',user_id=user_id))
        else:
            return render_template('reply_letter.html', letters =letter,user_id = user_id, letter_id=letter_id,form=form, error=error)  #may need modified
    if request.method == 'GET':
        return render_template('reply_letter.html',letters =letter,user_id = user_id, letter_id=letter_id,form=form)

@app.route('/signup/',methods=['GET','POST'])
def sign_up():
    error = None
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User(
                form.username.data,
                form.email.data,
                form.password.data,
            )
            try:
                db.session.add(new_user)
                db.session.commit()
                flash('Thanks for registering. Please login.')
                return redirect(url_for('login'))
            except IntegrityError:
                error = 'The username or email already exist. Please try again.'
                return render_template('register.html', form=form, error=error)
        else:
            return render_template('register.html', form=form, error=error)
    if request.method == 'GET':
        return render_template('register.html', form=form)

@app.route('/logout/')
@login_required
def log_out():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    flash('You are logged out. Bye. :(')
    return redirect(url_for('login'))




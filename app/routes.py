from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import app,db
from app.forms import newArtistForm, RegistrationForm, LoginForm, newEventForm, newVenueForm
from app.models import Artist,User,Event,Venue


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/artists')
def artists():
    artists = Artist.query.all()
    return render_template('artists.html', artists=artists, title='Artists')

@app.route('/artist/<name>')
def artist(name):
    artist = Artist.query.filter_by(name=name).first()
    return render_template('artist.html', artist=artist, title='Artist')

@app.route('/events')
def events():
    events = Event.query.all()
    return render_template('events.html', events=events, title='Events')

@app.route('/event/<name>')
def event(name):
    event = Event.query.filter_by(name=name).first()
    return render_template('event.html', event=event, title='Event')

@app.route('/addEvent', methods=['GET', 'POST'])
@login_required
def addEvent():
    form = newEventForm()
    if form.validate_on_submit():
        event = Event(name=form.eventName.data, eventVenue=form.venue.data, dateTime=form.dateTime.data)
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('events'))
    return render_template('addEvent.html', title='Add Venue', form=form)

@app.route('/addVenue', methods=['GET', 'POST'])
@login_required
def addVenue():
    form = newVenueForm()
    if form.validate_on_submit():
        flash('Venue submitted with name="{}" and location="{}"'.format(form.venueName.data, form.location.data))
        venue = Venue(name=form.venueName.data, location=form.location.data)
        db.session.add(venue)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addVenue.html', title='Add Venue', form=form)

@app.route('/addArtist', methods=['GET', 'POST'])
@login_required
def addArtist():
    form = newArtistForm()
    if form.validate_on_submit():
        flash('Artist submitted with name="{}", hometown="{}", and  bio="{}"'.format(form.artistName.data, form.hometown.data, form.bio.data))
        artist = Artist(name=form.artistName.data, hometown=form.hometown.data, bio=form.bio.data)
        db.session.add(artist)
        db.session.commit()
        return redirect(url_for('artists'))
    return render_template('addArtist.html', title='Add Artist', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password_hash=form.password.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now a registered user! UwU')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
            return redirect(next_page)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/populateDb')
def populateDb():
    a1 = Artist(name="Feed Me Jack", hometown="Oakland", bio="For about five years when they were active (from 2011 until 2016) they had released 4 eps on their own (e.g. via Bandcamp), and no other info around them actually.")
    a2 = Artist(name="Space Carnival", hometown="Oneonta", bio="High energy disco/funk band that provides many favorited covers")
    a3 = Artist(name="Peach Pit", hometown="Vancouver", bio="The Canadian band is led by singer and rhythm guitarist Neil Smith, lead guitarist Christopher Vanderkooy, bassist Peter Wilton, and drummer Mikey Pascuzzi. ... The band's music videos are produced by videographer Lester Lyons-Hookham.")
    v1 = Venue(name="The Haunt", location="Ithaca")
    v2 = Venue(name="Madison Square Garden", location="NYC")

    db.session.add_all([a1,a2,a3,v1,v2])
    db.session.commit()
    return "DB populated"

@app.route('/resetDb')
def resetDb():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table {}'.format(table))
        db.session.execute(table.delete())
    db.session.commit()
    populateDb()
    return "DB reset"
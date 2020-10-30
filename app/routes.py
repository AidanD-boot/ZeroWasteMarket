from flask import render_template, flash, redirect, url_for
from app import app,db
from app.forms import newArtistForm
from app.models import Artist


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

@app.route('/addArtist', methods=['GET', 'POST'])
def addArtist():
    form = newArtistForm()
    if form.validate_on_submit():
        flash('Artist submitted with name="{}", hometown="{}", and  bio="{}"'.format(form.artistName.data, form.hometown.data, form.bio.data))
        artist = Artist(name=form.artistName.data, hometown=form.hometown.data, bio=form.bio.data)
        db.session.add(artist)
        db.session.commit()
        return redirect(url_for('artists'))
    return render_template('addArtist.html', title='Add Artist', form=form)

@app.route('/populateDb')
def populateDb():
    a1 = Artist(name="Feed Me Jack", hometown="Oakland", bio="For about five years when they were active (from 2011 until 2016) they had released 4 eps on their own (e.g. via Bandcamp), and no other info around them actually.")
    a2 = Artist(name="Space Carnival", hometown="Oneonta", bio="High energy disco/funk band that provides many favorited covers")
    a3 = Artist(name="Peach Pit", hometown="Vancouver", bio="The Canadian band is led by singer and rhythm guitarist Neil Smith, lead guitarist Christopher Vanderkooy, bassist Peter Wilton, and drummer Mikey Pascuzzi. ... The band's music videos are produced by videographer Lester Lyons-Hookham.")

    db.session.add_all([a1,a2,a3])
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
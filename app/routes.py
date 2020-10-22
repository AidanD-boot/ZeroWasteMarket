from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import newArtistForm


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', title='Home')

@app.route('/artists.html')
def artists():
    artists = [
        {
            'author': {'username': 'Feed Me Jack'},
            'body': 'Feed Me Jack were a short-lived rock sextet / quintet hailing from Oakland, CA. For about five years when they were active (from 2011 until 2016) they had released 4 eps on their own (e.g. via Bandcamp), and no other info around them actually.'
        },
        {
            'author': {'username': 'Bobbing'},
            'body': 'This is a chunk of test characters to see if this works'
        },
        {
            'author': {'username': 'Still Woozy'},
            'body': 'This is a chunk of test characters to see if this works'
        }
    ]
    return render_template('artists.html', artists=artists, title='Artists')

@app.route('/artist.html')
def artist():
    abouts = [
        {
            'body': 'North American Tour starting year (2021)'
        },
        {
            'body': 'Release of a comeback album (2021)'
        },
        {
            'body': 'Reuniting the band finally after many years'
        },
        {
            'body': 'Doing it all for the fans :)'
        }
    ]
    return render_template('artist.html', abouts=abouts, title='Artist')

@app.route('/addArtist.html', methods=['GET', 'POST'])
def addArtist():
    form = newArtistForm()
    if form.validate_on_submit():
        flash('Artist submitted with name="{}" and bio="{}"'.format(form.artistName.data, form.bio.data))
        return redirect(url_for('index'))
    return render_template('addArtist.html', title='Add Artist', form=form)
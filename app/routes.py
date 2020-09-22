from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('base')

@app.route('/artists')
def artists():
    return render_template('artists')
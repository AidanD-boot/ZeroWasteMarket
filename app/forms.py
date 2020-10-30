from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class newArtistForm(FlaskForm):
    artistName = StringField('Artist name', validators=[DataRequired()])
    hometown = StringField('Hometown', validators=[DataRequired()])
    bio = StringField('Bio', validators=[DataRequired()])
    submit = SubmitField('Add Artist')
    
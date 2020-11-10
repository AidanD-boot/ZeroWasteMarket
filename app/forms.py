from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User, Venue

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username UwU')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address UwU')

class newArtistForm(FlaskForm):
    artistName = StringField('Artist name', validators=[DataRequired()])
    hometown = StringField('Hometown', validators=[DataRequired()])
    bio = StringField('Bio', validators=[DataRequired()])
    submit = SubmitField('Add Artist')

class newVenueForm(FlaskForm):
    venueName = StringField('Venue name', validators=[DataRequired()])
    location = StringField('City/Town', validators=[DataRequired()])
    submit = SubmitField('Add Venue', validators=[DataRequired()])

class newEventForm(FlaskForm):
    eventName = StringField('Event Name', validators=[DataRequired()])
    venue = SelectField('Event Venue', coerce=int ,validators=[DataRequired()])
    dateTime = DateTimeLocalField('Event Date', format='%m/%d/%y', validators=[DataRequired()])
    submit = SubmitField('Add Event', validators=[DataRequired()])

def edit_venue(request,id):
    venue = Venue.query.get(id)
    form = newEventForm(request.POST, obj=venue)
    form.venue.choices = [(v.id, v.name) for v in Venue.query.order_by('name')]
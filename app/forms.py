from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, FloatField, SelectMultipleField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Optional
from app.models import User

class ContentForm(FlaskForm):
    quantity = IntegerField('Quantity Requested', validators=[DataRequired()])
    submit = SubmitField('Add to Cart', validators=[DataRequired()])

class SupplierForm(FlaskForm):
    name = StringField('Business name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    zipcode = IntegerField('Zipcode', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    submit = SubmitField('Create New Supplier')

class ListingForm(FlaskForm):
    price = FloatField('Price', validators=[DataRequired()])
    quantity = IntegerField('Quantity Supplied', validators=[DataRequired()])
    produce = SelectField('Produce', validators=[DataRequired()])
    supplier = SelectField('Supplier', validators=[Optional()])
    submit = SubmitField('Create New Listing')

class ProduceForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    imageRef = StringField('Enter image link', validators=[DataRequired()])
    keywords = SelectMultipleField('Select All Keywords that Apply', validators=[Optional()])
    submit = SubmitField('Add New Produce Type')

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


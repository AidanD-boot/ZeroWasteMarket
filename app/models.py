from app import db,login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Produce(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, primary_key=True)
    imageRef = db.Column(db.String(128))
    listings = db.relationship('Listing', backref='lproduct', lazy='dynamic')
    keywords = db.relationship('ProduceToKeywords', backref='kproduct', lazy='dynamic')

    def __repr__(self):
        return '<Produce {} {}>'.formate(self.name, self.imageRef)

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    address = db.Column(db.String(64), index=True)
    zipcode = db.Column(db.Integer, index=True)
    city = db.Column(db.String(64), index=True)
    state = db.Column(db.String(64), index=True)
    listings = db.relationship('Listing', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<Supplier {} {} {} {} {}>'.format(self.name, self.address, self.city, self.state, self.zipcode)

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    produce_id = db.Column(db.Integer, db.ForeignKey('produce.id'))
    contents = db.relationship('Content', backref='list', lazy='dynamic')

    def __repr__(self):
        return '<Listing {} {}>'.format(self.price, self.quantity)

class ProduceToKeyword(db.Model):
    produce_id = db.Column(db.Integer, db.ForeignKey('produce.id'))
    keyword_id = db.Column(db.Integer, db.ForeignKey('keyword.id'))

class Keyword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    products = db.relationship('ProductToKeyword', backref='tag', lazy='dynamic')

    def __repr__(self):
        return '<Keyword {}>'.format(self.name)

class Content(db.Model):
    quantity = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    listing_id = db.Column(db.Integer, db.ForeignKey('listing.id'))

    def __repr__(self):
        return '<Content {}>'.format(self.quantity)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    contents =db.relationship('Content', backref='cart', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
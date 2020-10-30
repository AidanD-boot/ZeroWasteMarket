from app import db

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    hometown = db.Column(db.String(64), index=True)
    bio = db.Column(db.String(300), index=True)
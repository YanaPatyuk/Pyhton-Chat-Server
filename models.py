from . import db


class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), uniqe=True)
    password = db.Column(db.String(50))
    user_name = db.Column(db.String(50))


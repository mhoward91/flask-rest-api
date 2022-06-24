# model - internal representation of an entity - a helper which doesn't pollute API resources
# resource - external representation of an entity (what client sees)

import sqlite3
from db import db

# extends db.Model so SQLAlchemy can map between the database & these objects
class UserModel(db.Model):
    __tablename__ = "users"

    # defining a column by the variable name and its properties
    # it will then create an object for each row in the database
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


from flask_mongoengine import Document
from mongoengine.fields import EmailField, StringField
from flask_login import UserMixin


class User(Document, UserMixin):
    name = StringField(required=True, max_length=30, unique=True)
    email = EmailField(required=True, max_length=30, unique=True)
    password = StringField(required=True, max_length=100)
    user_type = StringField(required=True, max_length=10)

    def __repr__(self):
        return f'User({self.name}, {self.email}, {self.user_type}'



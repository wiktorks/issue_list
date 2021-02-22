from flask.globals import request
from flask_mongoengine import Document
from mongoengine.fields import EmailField, StringField
from flask_login import UserMixin

class User(Document, UserMixin):
    name = StringField(required=True, max_length=30)
    email = EmailField(required=True, max_length=30)
    password = StringField(required=True, max_length=100)
    user_type = StringField(required=True, max_length=10)
    meta = {
        'indexes': [
            'name',
            'email'
        ]
    }

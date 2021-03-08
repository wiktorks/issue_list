from flask_mongoengine import Document
from mongoengine.fields import ListField, ReferenceField, StringField
from .user import User

class BaseDocument(Document):
    name = StringField(required=True, max_length=30)
    author = ReferenceField(User)
    assigned_users = ListField(ReferenceField(User, reverse_delete_rule='CASCADE'))

    meta = {
        'allow_inheritance': True
    }

 
class Task(BaseDocument):
    description = StringField(max_length=500)


class Issue(BaseDocument):
    task_list = ListField(ReferenceField(Task))

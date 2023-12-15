from mongoengine import Document, StringField, DateTimeField, ListField, ReferenceField
from mongoengine import connect

connect(
    db='my-data-base',
    username='admin',
    password='51252cenia',
    host='cluster0.xvs4vtf.mongodb.net',
    port=27017,  # Порт (зазвичай 27017)
    authentication_source='admin',
    retryWrites=True,
    w='majority'
)

# Модель для колекції 'authors'
class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

# Модель для колекції 'quotes'
class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, required=True)
    quote = StringField()
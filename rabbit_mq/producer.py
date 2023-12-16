import pika
from mongoengine import connect, Document, StringField, BooleanField
from faker import Faker
import random

connect(
    db='my-data-base',
    username='admin',
    password='51252cenia',
    host='cluster0.xvs4vtf.mongodb.net',
    port=27017,
    authentication_source='admin',
    retryWrites=True,
    w='majority'
)

# Модель для контакту
class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    message_sent = BooleanField(default=False)

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue')


fake = Faker()


def generate_fake_contacts(count):
    contacts = []
    for _ in range(count):
        name = fake.name()
        email = fake.email()

        contact = {
            'name': name,
            'email': email,
            'sent_message': False

        }
        contacts.append(contact)
    return contacts


num_contacts = 10

fake_contacts = generate_fake_contacts(num_contacts)


connection.close()
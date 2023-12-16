import pika
from mongoengine import connect, Document
from bson import ObjectId



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

# Функція для імітації надсилання повідомлення
def send_email_contact(contact_id):

    contact = Contact.objects(id=ObjectId(contact_id)).first()
    if contact:

        print(f"Sending email to {contact.email}")

        contact.message_sent = True
        contact.save()
        print(f"Message sent to {contact.email}")


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue')

# Функція для обробки повідомлень з черги
def callback(ch, method, properties, body):
    send_email_contact(body.decode())
    print("Email sent for contact ID:", body.decode())

channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
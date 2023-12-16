# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
from models import Author, Quote
import json
"""
uri = "mongodb+srv://admin:51252cenia@cluster0.xvs4vtf.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

"""
with open('authors.json', 'r') as authors_file:
    authors_data = json.load(authors_file)


for author_info in authors_data:
    author = Author(
        fullname=author_info['fullname'],
        born_date=author_info['born_date'],
        born_location=author_info['born_location'],
        description=author_info['description']
    )
    author.save()


with open('quotes.json', 'r') as quotes_file:
    quotes_data = json.load(quotes_file)


for quote_info in quotes_data:
    author_name = quote_info['author']
    author = Author.objects(fullname=author_name).first()
    if author:
        quote = Quote(
            tags=quote_info['tags'],
            author=author,
            quote=quote_info['quote']
        )
        quote.save()
    else:
        print(f"Author '{author_name}' not found.")

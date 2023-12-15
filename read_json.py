import json


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
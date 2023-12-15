while True:
    command = input("Введіть команду (наприклад, 'name: Steve Martin', 'tag:life', 'tags:life,live' або 'exit'): ")

    if command.startswith('name:'):
        author_name = command.split('name: ')[1].strip()
        author = Author.objects(fullname=author_name).first()
        if author:
            quotes = Quote.objects(author=author)
            for quote in quotes:
                print(quote.quote)
        else:
            print(f"No quotes found for author '{author_name}'.")

    elif command.startswith('tag:'):
        tag = command.split('tag: ')[1].strip()
        quotes = Quote.objects(tags=tag)
        for quote in quotes:
            print(quote.quote)

    elif command.startswith('tags:'):
        tags = command.split('tags: ')[1].strip().split(',')
        quotes = Quote.objects(tags__in=tags)
        for quote in quotes:
            print(quote.quote)

    elif command == 'exit':
        break

    else:
        print("Невідома команда. Спробуйте ще раз.")
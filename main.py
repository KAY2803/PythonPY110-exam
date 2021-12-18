# генерация случайных книг

from faker import Faker
from faker.providers import isbn
import json
import random

import conf


def generate_books(pk=1):
    with open('book.txt', 'r', encoding='utf8') as f:
        name_book = f.read().split('\n')
    fake = Faker()
    Faker.seed(0)
    isbn = fake.isbn13()
    author_list = []
    for _ in range(3):
        author_list.append(fake.name())
    gen_fields = {}
    gen_fields = {
                      'Title': random.choice(name_book),
                      'year': random.randrange(1600, 2021),
                      'pages': random.randrange(10, 500),
                      'isbn13': isbn,
                      'rating': random.uniform(0, 5),
                      'price': random.uniform(10, 10000),
                      'author': random.sample(author_list, random.randint(1, 3))
    }
    final_gen_book = {
                        'model': conf.MODEL,
                        'pk': pk,
                        'fields': gen_fields
    }

    yield gen_fields

if __name__ == "__main__":


    def final_gen_book(pk=1):
        for _ in range(5):
            fields = next(generate_books())
            with open('gen_book', 'w', encoding='utf-8') as file:
                for _ in range(5):
                    books = {
                            'model': conf.MODEL,
                            'pk': pk,
                            'fields': fields
                    }
            pk += 1
            return json.dump(books, file, ensure_ascii=False, indent=4)








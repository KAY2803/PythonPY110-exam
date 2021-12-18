# генерация случайных книг

from faker import Faker
from faker.providers import isbn
import json
import random

import conf


def generate_fields():
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
                      'pages': random.randrange(10, 10000),
                      'isbn13': isbn,
                      'rating': float(f'{random.uniform(0, 5):.2f}'),
                      'price': float(f'{random.uniform(10, 10000):.2f}'),
                      'author': random.sample(author_list, random.randint(1, 3))
    }

    yield gen_fields


if __name__ == "__main__":


    def gen_books(pk=1):
        with open('gen_book', 'w', encoding='utf-8') as file:
            for _ in range(3):
                books = {
                        'model': conf.MODEL,
                        'pk': pk,
                        'fields': next(generate_fields())
                }
                pk += 1
                json.dump(books, file, ensure_ascii=False, indent=4)


    gen_books()








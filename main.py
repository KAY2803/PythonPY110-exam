# генерация случайных книг

from faker import Faker
from faker.providers import isbn
import json
import random
from typing import Iterator

import conf


def title() -> Iterator:
    """Из текстового файла 'book.txt' выбирается одна из книг.

    Содержание файла (названия книг из 'book.txt) записывается в переменную 'name_book' (list).
    С помощью random функция возвращает одно из значений, записанных в переменную 'name_book'
    """

    with open('book.txt', 'r', encoding='utf8') as f:
        name_book = f.read().split('\n')
        yield random.choice(name_book)


def year() -> Iterator:
    """C помощью random задается параметр 'year' (год) для словаря с данными о книге"""
    yield int(random.randrange(1600, 2021))


def pages() -> Iterator:
    """C помощью random задается параметр 'pages' (кол-во страниц) для словаря с данными о книге"""
    yield int(random.randrange(10, 10000))


def isbn_() -> Iterator:
    """C помощью faker и random задается параметр 'isbn' (код) для словаря с данными о книге"""
    fake = Faker()
    Faker.seed(0)
    yield fake.isbn13()


def rating() -> Iterator:
    """C помощью random задается параметр 'rating' (рейтинг) для словаря с данными о книге"""
    yield float(f'{random.uniform(0, 5):.2f}')


def price() -> Iterator:
    """C помощью random задается параметр 'price' (цена) для словаря с данными о книге"""
    yield float(f'{random.uniform(10, 10000):.2f}')


def author() -> Iterator:
    """C помощью faker и random задается параметр 'author' (авторы) для словаря с данными о книге"""
    fake = Faker()
    for _ in range(random.randrange(1, 4)):
        yield fake.name()


if __name__ == "__main__":


    def gen_books(pk: int = 1) -> []:
        """Функция создает список словарей с данными о книге.

        Именнованный аргумент pk - счетчик количества созданных словарей, по умолчанию = 1.
        Переменная 'book' - словарь с данными о книге
        """

        with open('gen_book', 'w', encoding='utf-8') as file:
            for _ in range(3):
                book = {
                        'model': conf.MODEL,
                        'pk': pk,
                        'fields': {'title': next(title()),
                                   'year': next(year()),
                                   'pages': next(pages()),
                                   'isbn': next(isbn_()),
                                   'rating': next(rating()),
                                   'price': next(price()),
                                   'author': next(author())
                        }
                }
                pk += 1
                json.dump(book, file, ensure_ascii=False, indent=4)


    gen_books()








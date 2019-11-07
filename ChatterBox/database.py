import datetime

from peewee import *

db = SqliteDatabase('../database.db')


class User(Model):
    login = CharField()
    password = CharField()
    country = CharField()
    phone_number = CharField()
    website = CharField()
    favourite_quote = CharField()
    favourite_book_author = CharField()

    class Meta:
        database = db


class Messages(Model):
    from_id = ForeignKeyField(User)
    content = CharField()
    created_at = DateTimeField()

    class Meta:
        database = db


def check_auth(login, password) -> bool:
    return bool(User.select().where(User.login == login, User.password == password.encode()))


def is_unique(login) -> bool:
    return bool(User.get(User.login == login))


def add_user(login, password, country='', phone='', website='', quote='', author=''):
    user = User(login=login, password=password, country=country, phone_number=phone, website=website,
                favourite_quote=quote, favourite_book_author=author)
    user.save()


def add_message(content, login, date):
    user = User.get(User.login == login)
    date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    message = Messages(from_id=user.id, content=content, created_at=date)
    message.save()


def edit_user_info(login, new_login='', password='', country='', phone='', website='', quote='', author=''):
    user = User.get(User.login == login)
    if new_login:
        user.login = new_login
    if password:
        user.password = password
    if country:
        user.country = country
    if phone:
        user.phone_number = phone
    if website:
        user.website = website
    if quote:
        user.favourite_quote = quote
    if author:
        user.favourite_book_author = author
    user.save()


def get_names():
    return [user.login for user in list(User.select())]


def get_user(login):
    return User.get(User.login == login)

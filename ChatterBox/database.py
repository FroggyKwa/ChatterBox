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


def check_unique(login) -> bool:
    return bool(User.select().where(User.login == login))


def add_user(login, password):
    user = User(login=login, password=password)
    user.save()


def add_message(content, login, date):
    user = User.get(User.login == login)
    date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    message = Messages(from_id=user.id, content=content, created_at=date)
    message.save()


db.create_tables([User, Messages])

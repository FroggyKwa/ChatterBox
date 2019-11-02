from peewee import *
from hashlib import md5

db = SqliteDatabase('../database.db')


class User(Model):
    login = CharField()
    password = CharField()

    class Meta:
        database = db


class Messages(Model):
    from_id = ForeignKeyField(User)
    content = CharField()
    created_at = DateField()

    class Meta:
        database = db


def check_auth(login, password) -> bool:
    return bool(User.select().where(User.login == login, User.password == password.encode()))


def check_unique(login) -> bool:
    return bool(User.select().where(User.login == login))


# TODO: доделать проверку на наличие пользователя в db


def add_user(login, password):
    user = User(login=login, password=password)
    user.save()

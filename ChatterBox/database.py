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


def in_database(login, password) -> bool:
    if User.select().where(User.login == login, User.password == md5(password.encode()).hexdigest()):
        return True

# TODO: доделать проверку на наличие пользователя в db


def add_user(login, password):
    user = User(login=login, password=password)
    user.save()

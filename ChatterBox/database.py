from peewee import *

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


def check_unique(login, password) -> bool:
    if not User.select().where(User.login == login, User.password == password):
        return False
    return True


def add_user(login, password):
    user = User(login=login, password=password)
    user.save()


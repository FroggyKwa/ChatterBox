from _md5 import md5

from peewee import *

db = SqliteDatabase('../database.db')


class User(Model):
    id = AutoField(primary_key=True)
    login = CharField()
    password = CharField()

    class Meta:
        database = db


class Messages(Model):
    id = AutoField(primary_key=True)
    from_id = ForeignKeyField(User)
    content = CharField()
    created_at = DateField()

    class Meta:
        database = db


def auth(login, password) -> bool:
    if not User.select().where(User.login == login and User, User.password == password):
        return False
    return True


def add_user(login, password):
    user = User(login, password)
    user.save()


User.create_table()
Messages.create_table()

# TODO: Допилить add_user, разботать autoincrement id

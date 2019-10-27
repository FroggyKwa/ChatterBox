from peewee import *

db = SqliteDatabase('../database.db')


class User(Model):
    id = IntegerField(primary_key=True)
    login = CharField()
    password = CharField()

    class Meta:
        database = db


class Messages(Model):
    id = IntegerField()
    from_id = ForeignKeyField(User)
    content = CharField()
    created_at = DateField()

    class Meta:
        database = db


User.create_table()
Messages.create_table()

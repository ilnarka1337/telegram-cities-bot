from peewee import *

db=SqliteDatabase('database.db')
cursor=db.cursor()

class User(Model):
    user_id=IntegerField()
    bot_city=CharField()
    user_city=CharField()
    old_cities=CharField()

    class Meta:
        database=db

User.create(user_id = i td)
123
123
current_user=User.get(User.user_id == )
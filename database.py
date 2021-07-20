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


def update_bot_city(user_id : int, city : str):
    current_user = User.get(User.user_id == user_id)
    current_user.bot_city = city
    current_user.save()


User.create(user_id = i td)
current_user=User.get(User.user_id == )
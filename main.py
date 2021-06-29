"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging, configs, city_game, bot_config

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = bot_config.API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer("Привет, я бот, в котором можно поиграть в различные приколюхи :) Пока что есть только"
                        " игра в города, так что пиши /cities и вперед!")


@dp.message_handler(commands=['cities'])
async def start_cities(message: types.Message):
    await message.reply("Ты решил сыграть со мной в города? А ты смельчак! Тогда вперёд!")
    configs.cities_state=1
    rnd_city = city_game.generate_rnd_city()
    while rnd_city is None:
        rnd_city = city_game.generate_rnd_city()
    await message.answer("Начнём, мой город = " + rnd_city[0] + "\nТебе на " + str(rnd_city[0][-1].upper()))



@dp.message_handler()
async def echo(message: types.Message):
    user_city=str(message.text)
    # await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

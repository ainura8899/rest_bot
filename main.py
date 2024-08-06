
from aiogram import Bot, Dispatcher,types
from aiogram.filters import Command
import asyncio
from os import getenv
from dotenv import load_dotenv
# import logging
import random


load_dotenv()
token = getenv('BOT_TOKEN')
bot = Bot(token=token)
dp = Dispatcher()

recipes = [['bliny',['milk','eggs','sugar','flour']],
           ['sharlotka',['kefir','eggs','sugar','flour','apple']],
           ['greek salad',['tomato','cucumber','cheese','sweet pepper','olives']]]

@dp.message(Command('start'))
async def start(message: types.Message):
    # print(vars(message.from_user))
    await message.answer(f'Привет, {message.from_user.first_name}, я бот группы Гармония вкуса')


@dp.message(Command('my_info'))
async def my_info(message: types.Message):
    print(vars(message.from_user))
    await message.answer(f'Ваш ID: {message.from_user.id}\n '
                         f'имя: {message.from_user.first_name}\n'
                         f'username: {message.from_user.username}')

@dp.message(Command('random_recipe'))
async def random_recipe(message: types.Message):
    random_recipee = random.choice(recipes)
    await message.answer(f'{random_recipee[0]}\n'
                         f'{random_recipee[1]}\n')

async def main():
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


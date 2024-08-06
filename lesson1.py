
from aiogram import Bot, Dispatcher,types
from aiogram.filters import Command
import asyncio
from os import getenv
from dotenv import load_dotenv
# import logging



load_dotenv()
token = getenv('BOT_TOKEN')
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command('start'))
async def start_command_handler(message: types.Message):
    # print(vars(message.from_user))
    await message.answer(f'Привет, {message.from_user.first_name}, я бот группы Гармония вкуса')


@dp.message(Command('picture'))
async def picture_handler(message: types.Message):
    image = types.FSInputFile('images/Скумбрия в лаваше.jpg')
    await message.answer_photo(
        photo=image,
        caption='Скумбрия в лаваше'
    )


@dp.message()
async def echo_handler(message: types.Message):
    await message.reply(message.text)

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(message.text)

async def main():
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
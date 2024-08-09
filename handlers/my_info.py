from config import bot,dp
from aiogram import types, Router, F
from aiogram.filters import Command


my_info_router=Router()


@my_info_router.message(Command('my_info'))
async def my_info(message: types.Message):
    print(vars(message.from_user))
    await message.answer(f'Ваш ID: {message.from_user.id}\n '
                         f'имя: {message.from_user.first_name}\n'
                         f'username: {message.from_user.username}')
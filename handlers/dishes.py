from config import bot,dp
from aiogram import types, Router, F
from aiogram.filters import Command
import random
from aiogram.types import FSInputFile


dishes_router=Router()

@dishes_router.message(F.text=='Холодные напитки')
async def drinks(message: types.Message):
    photo=FSInputFile('images/mohito.jpg')
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo,
        caption='Черничный мохито'
    )
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=FSInputFile('images/tea.jpg'),
        caption='Холодный чай'
    )
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=FSInputFile('images/lemonade.jpg'),
        caption='Лимонад'
    )

@dishes_router.message(F.text=='Блюда')
async def drinks(message: types.Message):
    photo=FSInputFile('images/plov.jpg')
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo,
        caption='Плов'
    )
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=FSInputFile('images/Bliny.jpg'),
        caption='Блины'
    )
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=FSInputFile('images/greek salad.jpg'),
        caption='Салат Греческий'
    )
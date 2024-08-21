from config import bot,dp, database
from aiogram import types, Router, F
from aiogram.filters import Command
import random
from aiogram.types import FSInputFile


menu_router = Router()


@menu_router.message(Command('menu'))
async def menu(message: types.Message):
    kb=types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text = 'Напитки', callback_data='drinks')],
            [types.InlineKeyboardButton(text = 'Блюда', callback_data='dishes')],
            [types.InlineKeyboardButton(text='Салаты', callback_data='salads')],
        ]
    )
    await message.answer('Выберите категорию', reply_markup=kb)

signal = ('drinks', 'dishes', 'salads')

@menu_router.callback_query(lambda call:call.data in signal)
async def dishes(call:types.CallbackQuery):
    query='''
    SELECT * FROM dishes JOIN categories ON dishes.category_id = categories.id WHERE categories.name =?'''

    data=database.fetch(
        query=query,
        params=(call.data,),
    )
    for i in data:
        photo = FSInputFile(i[3])
        await call.message.answer_photo(photo=photo, caption=f'Наименование: {i[1]}\n'
                                        f'Цена: {i[2]}\n')
from config import bot,dp
from aiogram import types, Router, F
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command('start'))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://navat.kg/"),
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://www.instagram.com/navat_kg/")
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us")
            ],
            [
                types.InlineKeyboardButton(text="Отзывы", callback_data="review")
            ],
            [
                types.InlineKeyboardButton(text="Наши вакансии", callback_data="vacancies")
            ],
            [
                types.InlineKeyboardButton(text="Оставить отзыв", callback_data="feedback")
            ]

        ]
    )
    await message.answer(f'Привет, {message.from_user.first_name}', reply_markup=kb)
@start_router.callback_query(F.data=='about_us')
async def about_us(call: types.callback_query):
    await call.answer(f'Чайхана Navat - оазис восточной культуры, где гости испытывают уникальное путешествие'
                             f'через изумительные вкусы, аутентичную эстетику и безупречное гостеприимство.')

@start_router.callback_query(F.data=='review')
async def feedback(call: types.callback_query):
    await call.answer(f'Это лучший ресторан для знакомства с кухней Киргизии.')

@start_router.callback_query(F.data=='vacancies')
async def vacancies(call: types.callback_query):
    await call.answer(f'Требуются: официант, помощник повара.')
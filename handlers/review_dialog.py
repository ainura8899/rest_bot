import datetime

from config import bot,dp
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from datetime import datetime


class RestaurantReview(StatesGroup):
    name = State()
    instagram_username = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()

review_router = Router()

@review_router.callback_query(F.data=='feedback')
async def start_review(Callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(RestaurantReview.name)
    await Callback.answer()
    await bot.send_message(Callback.from_user.id, text ="Ваше имя: " )

@review_router.message(RestaurantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RestaurantReview.instagram_username)
    await message.answer("Ваш инстаграм логин: ")

@review_router.message(RestaurantReview.instagram_username)
async def process_instagram(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    await state.set_state(RestaurantReview.visit_date)
    await message.answer("Дата посещения: ")

@review_router.message(RestaurantReview.visit_date)
async def process_visit_date(message: types.Message, state: FSMContext):
    await state.update_data(date=message.text)
    await state.set_state(RestaurantReview.food_rating)
    kb = types.ReplyKeyboardMarkup(
        keyboard = [
            [types.KeyboardButton(text='плохо')],
            [types.KeyboardButton(text='хорошо')],
        ]
    )
    await message.answer('Качество еды: ', reply_markup=kb)

@review_router.message(RestaurantReview.food_rating)
async def food_rating(message: types.Message, state: FSMContext):
    food_rating = message.text
    if food_rating =='плохо' or food_rating =='хорошо':
        await state.update_data(food_rating=message.text)
        await state.set_state(RestaurantReview.cleanliness_rating)
        kb = types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton(text='плохо')],
                [types.KeyboardButton(text='хорошо')],
            ]
        )
        await message.answer('Рейтинг чистоты: ', reply_markup=kb)
    else:
        await message.answer("Вводите только 'хорошо' или 'плохо'")
    return



@review_router.message(RestaurantReview.cleanliness_rating)
async def process_cleanliness_rating(message: types.Message, state:FSMContext):
    cleanliness_rating = message.text
    if cleanliness_rating == 'плохо' or cleanliness_rating == 'хорошо':
        await state.update_data(cleanliness_rating=message.text)
        await state.set_state(RestaurantReview.extra_comments)
        kb = types.ReplyKeyboardRemove()
        await message.answer('Ваши комментарии: ', reply_markup=kb)
    else:
        await message.answer("Вводите только 'хорошо' или 'плохо'")
    return


@review_router.message(RestaurantReview.extra_comments)
async def process_extra_comments(message: types.Message, state:FSMContext):
    await state.update_data(extra_comments=message.text)
    await message.answer('Ваши комментарии приняты.')
    data = await state.get_data()
    await state.clear()
    print(data)
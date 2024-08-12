from config import bot,dp
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class RestaurantReview(StatesGroup):
    name = State()
    instagram_username = State()
    visit_date = State()
    food_rating = State()
    cleanliess_rating = State()
    extra_comments = State()

review_router = Router()

@review_router.callback_query(F.data=='feedback')
async def start_review(call:types.CallbackQuery, state:FSMContext):
    await state.set_state(RestaurantReview.name)
    await call.message.answer("Ваше имя: ")

@review_router.message(RestaurantReview.name)
async def process_name(message:types.Message, state:FSMContext):
    await message.answer("Ваш инстаграм логин: ")
    await state.set_state(RestaurantReview.instagram_username)

@review_router.message(RestaurantReview.instagram_username)
async def process_instagram(message:types.Message, state:FSMContext):
    await message.answer("Дата посещения: ")
    await state.set_state(RestaurantReview.visit_date)

@review_router.message(RestaurantReview.visit_date)
async def process_visit_date(message:types.Message, state:FSMContext):
    await state.set_state(RestaurantReview.food_rating)
    kb = types.ReplyKeyboardMarkup(
        keyword = [
            [types.KeyboardButton(text='плохо')],
            [types.KeyboardButton(text='хорошо')],
        ]
    )
    await message.answer('Качество еды: ', reply_markup=kb)

@review_router.message(RestaurantReview.food_rating)
async def food_rating(message: types.Message, state:FSMContext):
    await state.set_state(RestaurantReview.cleanliess_rating)
    kb = types.ReplyKeyboardMarkup(
        keyword=[
            [types.KeyboardButton(text='плохо')],
            [types.KeyboardButton(text='хорошо')],
        ]
    )
    await message.answer('Рейтинг чистоты: ', reply_markup=kb)


@review_router.message(RestaurantReview.cleanliess_rating)
async def process_cleanliess_rating(message:types.Message, state:FSMContext):
    await state.set_state(RestaurantReview.extra_comments)
    kb = types.ReplyKeyboardRemove()
    await message.answer('Ваши комментарии: ', reply_markup=kb)

@review_router.message(RestaurantReview.extra_comments)
async def process_extra_comments(message: types.Message, state:FSMContext):
    await message.answer('Ваши комментарии приняты.')
    await state.clear()
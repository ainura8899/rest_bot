import datetime

from config import bot,dp
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from datetime import datetime
from config import database
from Database.queries import Queries

review_router = Router()

class Opros(StatesGroup):
    name = State()
    age = State()
    gender = State()
    occupation = State()


@review_router.callback_query(F.data=='feedback')
async def start_review(Callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Opros.name)
    await Callback.answer()
    await bot.send_message(Callback.from_user.id, text ="Ваше имя: " )

@review_router.message(Opros.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Opros.age)
    await message.answer("Ваш возраст: ")

@review_router.message(Opros.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Вводите только цифры")
        return
    if age < 17:
        break
    else:
        await state.update_data(age=message.text)
        await state.set_state(Opros.gender)
        await message.answer("Ваш пол: ")

@review_router.message(Opros.gender)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(Opros.occupation)
    await message.answer("Ваше занятие: ")


@review_router.message(Opros.occupation)
async def process_occupation(message: types.Message, state:FSMContext):
    await state.update_data(occupation=message.text)
    await message.answer('Ваши данные приняты.')
    data = await state.get_data()
    await state.clear()
    print(data)

    database.execute(Queries.INSERT_INTO_OPROS, (None, data["name"], data["age"], data["gender"], data["occupation"]))



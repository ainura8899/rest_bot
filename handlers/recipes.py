from config import bot,dp
from aiogram import types, Router
from aiogram.filters import Command
import random

recipe_router = Router()

recipes = [['bliny',['milk','eggs','sugar','flour']],
           ['sharlotka',['kefir','eggs','sugar','flour','apple']],
           ['greek salad',['tomato','cucumber','cheese','sweet pepper','olives']]]

@recipe_router.message(Command('random_recipe'))
async def random_recipe(message: types.Message):
    random_recipee=random.choice(recipes)
    await message.answer(f'{random_recipee[0]}\n'
                         f'{random_recipee[1]}\n')


from aiogram import Router, F, types
from aiogram.filters.command import Command
from config import bot
from datetime import timedelta


group_router = Router()
group_router.message.filter(F.chat.type != 'private')

BAD_WORDS = {"дурак", "идиот", "козел"}


@group_router.message(Command("ban", prefix="!"))
async def ban_group_user(message: types.Message):
    print(message.text)
    print(message.from_user.first_name)
    reply = message.reply_to_message
    if reply:
        await bot.ban_chat_member(
            chat_id=message.chat.id,
            user_id=reply.from_user.id,
            until_date=timedelta(seconds=120)
        )


@group_router.message()
async def filter_bad_words(message: types.Message):
    print(message.chat.type)
    txt = message.text
    for word in BAD_WORDS:
        if word in txt.lower():
            await message.answer(
                f"Пользователь {message.from_user.first_name} использовал запрещенное слово"
            )
            await message.delete()
            break
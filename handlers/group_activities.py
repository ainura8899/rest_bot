from aiogram import Router, F, types
from aiogram.filters.command import Command
from config import bot
from datetime import timedelta


group_router = Router()
group_router.message.filter(F.chat.type != 'private')

BAD_WORDS = ["дурак", "идиот", "козел"]

# @group_router.message(Command("ban", prefix="!"))
# async def ban_group_user(message: types.Message):
#     print(message.text)
#     print(message.from_user.first_name)
#     # reply = message.reply_to_message
#     # if reply:
#         await bot.ban_chat_member(
#             chat_id=message.chat.id,
#             user_id=reply.from_user.id,
#             until_date=timedelta(seconds=120)
#         )

@group_router.message(lambda m:m.text.lower() in BAD_WORDS)
async def filter_bad_words(message: types.Message):
    await message.answer(
         f"Пользователь {message.from_user.first_name} использовал запрещенное слово"
    )
    await bot.ban_chat_member(
         chat_id=message.chat.id,
         user_id=message.from_user.id,
         until_date=timedelta(seconds=120)
    )
    await message.delete()

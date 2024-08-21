import asyncio
import logging

from config import bot, dp, database   # set_bot_commands
from handlers.echo import echo_router
from handlers.start import start_router
from handlers.recipes import recipe_router
from handlers.my_info import my_info_router
from handlers.dishes import dishes_router
from handlers.review_dialog import review_router
from handlers.menu import menu_router

async def on_startup(bot):
    print ("Бот запустился")
    database.create_tables()


async def main():
    # await set_bot_commands()
    # добавляем маршрутизаторы диспетчеру
    dp.include_router(start_router)
    dp.include_router(recipe_router)
    dp.include_router(my_info_router)
    dp.include_router(dishes_router)
    dp.include_router(review_router)
    dp.include_router(menu_router)

    # в самом конце
    dp.include_router(echo_router)

    dp.startup.register(on_startup)
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


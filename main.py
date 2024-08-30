import asyncio
import logging

from config import bot, dp, database   # set_bot_commands
from handlers import(
    private_router,
    group_router,
    house_router
)


async def on_startup(bot):
    print ("Бот запустился")
    database.create_tables()


async def main():
    # await set_bot_commands()
    # добавляем маршрутизаторы диспетчеру
    dp.include_router(private_router)
    dp.include_router(group_router)
    # dp.include_router(recipe_router)
    # dp.include_router(my_info_router)
    # dp.include_router(dishes_router)
    # dp.include_router(review_router)
    # dp.include_router(menu_router)


    dp.startup.register(on_startup)
    # в самом конце
    # dp.include_router(echo_router)


    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


import asyncio
import logging

from config import bot, dp, database   # set_bot_commands
from handlers import(
    private_router,
   )


async def on_startup(bot):
    print ("Бот запустился")
    database.create_tables()


async def main():
    # await set_bot_commands()
    # добавляем маршрутизаторы диспетчеру
    dp.include_router(private_router)
    dp.include_router(review_router_name)
    dp.include_router(private_router_age)
    dp.include_router(private_router_gender)
    dp.include_router(private_router_gender)


    # в самом конце
    # dp.include_router(echo_router)

    dp.startup.register(on_startup)
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


from aiogram import Router, types
from aiogram.filters.command import Command
from crawler.house_kg import HouseCrawler


house_router = Router()

@house_router.message (Command("houses"))
async def show_new_houses_handler(message: types.Message):
    crawler = HouseCrawler()
    crawler.get_page()
    links = crawler.get_house_links()
    for link in links:
        await message.answer(link)


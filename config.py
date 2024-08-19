from aiogram import Bot, Dispatcher, types
from os import getenv
from dotenv import load_dotenv
from Database.database import Database

load_dotenv()

token = getenv('TOKEN')
bot = Bot(token=token)
dp = Dispatcher()
database = Database("db.sqlite3")

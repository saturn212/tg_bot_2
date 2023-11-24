from aiogram import Bot, Dispatcher, Router
import sqlite3
TOKEN = '6901180948:AAHEKUlzcYlyp0KedssphMzfKvYU3XoacTU'
router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(TOKEN, parse_mode="HTML")
con = sqlite3.connect('data.db')
cursor = con.cursor()

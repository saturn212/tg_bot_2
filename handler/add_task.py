from aiogram import types
from aiogram.filters import Text, Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from loader import *
from keys.key import kb_menu
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class Task_form(StatesGroup):
    task = State()

@router.message(Command("cancel"))
async def cancel(message: types.Message, state:FSMContext):
    await state.clear()
    await message.answer('Действие отменено')

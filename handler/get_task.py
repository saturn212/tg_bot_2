from aiogram import types
from aiogram.filters import Text
from loader import *

@router.message(Text("Список задач"))
async def get_task(message: types.Message):
    id_user = message.chat.id
    cursor.execute(('SELET * FROM task WHERE id = (?)', [id_user]))
    data = cursor.fetchall()[0]
    text = ''
    num = 1
    for i in range (2, len(data)):
        if data[i] != '-':
            text += f'{num}) {data[1]}.\n'
            num += 1
    if text:
        await message.answer(text=f'Ваш список задач:\n{text}')
    else:
        await message.answer(text=f'Список задач пуст')
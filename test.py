from config import tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer('Привет! Напиши, сколько символов должно быть в пароле? (Макс. 74)')

@dp.message_handler()
async def get_password(message: types.Message):
    passlength = message.text
    try:
        passlength = int(passlength)
        if passlength > 74 or passlength < 0:
            await message.reply('Необходимо ввести числа от 1 до 74')
        else:
            a = 'abcdefghijklmnopqrstuvwxyz'
            b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            c = '0123456789'
            d = '!@#$%^&*()_+=-'
            all = ((a + b + c + d)*999999)
            password = ''.join(random.sample(all, passlength))
            await message.answer(f'Ваш пароль: {password}')
    except Exception as ex2:
        print(ex2)
        await message.answer('Необходимо ввести числа от 1 до 74')
if __name__ == '__main__':
    executor.start_polling(dp)

    """@dp.message_handler()
    async def get_password(message: types.Message):
    	types = int(types)"""

    """try:
        passlength = int(passlength)
        if passlength > 74 or passlength < 0:
            await message.reply('Недопустимый размер пароля')
            else:
            a = 'abcdefghijklmnopqrstuvwxyz'
            b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            c = '0123456789'
            alls = a + b + c
            password = ''.join(random.sample(alls, passlength))
            await message.answer(f'Ваш пароль: {password}')
            except Exception as ex2:
            print(ex2)
            await message.answer("Необходимо ввести числа от 1 до 74")
    elif gen == "1":
        @dp.message_handler()
        async def get_password(message: types.Message):
            passlength = message.text
            try:
                passlength = int(passlength)
                if passlength > 13 or passlength < 3:
                    await message.reply('Недопустимый размер PIN-кода')
                else:
                    c = '0123456789' * 100000
                    password = ''.join(random.sample(с, passlength))
                    await message.answer(f'Ваш PIN-код: {password}')
            except Exception as ex2:
                print(ex2)
                await message.answer("Необходимо ввести числа от 4 до 12")
    else:
        await message.answer('Введите 1 или 2')"""
from config import tg_bot_token
from aiogram import Bot, types, Dispatcher, executor
from aiogram.utils.markdown import hstrikethrough, hbold, hunderline, hitalic, hcode
import random
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(token=tg_bot_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
	global your_name
	your_name = message.from_user.username
	await bot.send_animation(chat_id=message.chat.id, animation=open("Rules.gif", "rb"),
							caption=f"Добро пожаловать в {hstrikethrough('бойцовский клуб')} клуб создания паролей."
									f" Запомни, первое правило клуба — {hbold('не разглашать пароли третьим лицам')}.\n\n"
									f"Второе правило клуба: {hbold('пароль принадлежит только одному')}.\n\nЭто понятно? Чтобы сгенерировать пароль, введи две цифры в следующем формате:\n \n"
									f"{hcode('x,y - где x это длина пароля, а y - это способ (PIN-код == 1, пароль == 2)')}\n \n"
									f" {hitalic(f'Удачи, {your_name}!')}")

@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
	await bot.send_animation(chat_id=message.chat.id, animation=open("Tired.gif", "rb"),
							 caption=f"Неужели непонятно? Так уж и быть, расскажу. Этот бот генерирует пароли заданной пользователем длины, используя"
									 f" английский алфавит ({hunderline('в нижнем и верхних регистрах')}), цифры и специальные символы. ")
@dp.message_handler()
async def passwordLength(message: types.Message):
	xy_values = message.text.split(",")
	global lengthOfPassword
	lengthOfPassword = xy_values[0]
	lengthOfPassword = int(lengthOfPassword)
	global typeOfGenerator
	typeOfGenerator = xy_values[1]
	typeOfGenerator = int(typeOfGenerator)
	print(f"|{typeOfGenerator}|{lengthOfPassword}|")
	try:
		if typeOfGenerator == 1:
			numbers = ("0123456789" * 100000)
			pincode = "".join(random.sample(numbers, lengthOfPassword))
			await bot.send_animation(chat_id=message.chat.id, animation=open("YouGotIt.gif", "rb"),
									 caption=f"Ваш PIN-код с длиной {lengthOfPassword}: {hcode(pincode)} — можете скопировать нажатием на текст. {hbold('Тайлер Дерден')} гордится тобой, {your_name}!")
		elif typeOfGenerator == 2:
			englishLowercaseLetters = "abcdefghijklmnopqrstuvwxyz"
			englishUppercaseLetters = englishLowercaseLetters.upper()
			digits = "0123456789"
			specialSymbols = "[]{}()/,_!?\""
			output = "".join(random.sample(englishUppercaseLetters + englishUppercaseLetters + digits + specialSymbols,
								   lengthOfPassword))
			await bot.send_animation(chat_id=message.chat.id, animation=open("YouGotIt.gif", "rb"),
									 caption=f"Ваш PIN-код с длиной {lengthOfPassword}: {hcode(output)} — можете скопировать нажатием на текст. {hbold('Тайлер Дерден')} гордится тобой, {your_name}!")
	except Exception as ex2:
		print(ex2)
		await bot.send_animation(chat_id=message.chat.id, animation=open("Dissapointed.gif", "rb"),
								caption=f"Значит так. Дано три варианта:\n"
										f"1. Не указали значения как в примере: x,y (без пробелов и сразу после запятой число) \n"
										f"2. Я не предусмотрел :) \n"
										f"3. Слишком большое значение в длине пароля, которое выходит за количество символов (около ~50) \n"
										f"\n"
										f"{hunderline('В любом случае, возвращайся на /start и повторяй снова!')}")

if __name__ == '__main__':
	executor.start_polling(dp)
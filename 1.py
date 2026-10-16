import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

from button import main_buttons, school_buttons

bot = Bot(token="8664320593:AAHytvGLn5PgDeTzFULtVqlwk__Fws8WFJ4")
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: Message):
    full_name = message.from_user.full_name
    await message.answer(f"Xush kelibsiz {full_name} zoti oliylari!",
    reply_markup=await main_buttons())


@dp.message(F.text == "📚 Maktab darsliklari")
async def reaction_to_schoo_lessons(message: Message):
    return message.answer("Sinfni tanlang!", reply_markup=await school_buttons())


@dp.message(F.text == "Go Back")
async def reaction_to_go_back(message: Message):
    await message.answer("Asosiy sahifa", reply_markup=await main_buttons())



@dp.message(F.text == "📙 1-sinf darsliklari")
async def reaction_to_go_back(message: Message):
    await message.answer("Asosiy sahifa", reply_markup=await main_buttons())


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
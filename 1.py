import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from button import main_buttons, school_buttons, it_buttons

bot = Bot(token="8668894494:AAF0mcmvCzrIqB4yVIpD2ja6l4yk17pec2I")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    full_name = message.from_user.full_name
    await message.answer(
        f"Xush kelibsiz {full_name}!",
        reply_markup=await main_buttons()
    )



@dp.message(F.text == "📚 Maktab darsliklari")
async def reaction_to_school_lessons(message: Message):
    await message.answer(
        "Sinfni tanlang!",
        reply_markup=await school_buttons()
    )



@dp.message(F.text == "Go Back")
async def reaction_to_go_back(message: Message):
    await message.answer(
        "Asosiy sahifa",
        reply_markup=await main_buttons()
    )



@dp.message(F.text.startswith("📙 ") & F.text.endswith("-sinf darsliklari"))
async def reaction_to_lessons(message: Message):

    if message.text == "📙 1-sinf darsliklari":
        file1 = FSInputFile("1-sinf.pdf")
        photo1 = FSInputFile("1-sinf.webp")
        await message.answer_document(file1)
        await message.answer_photo(photo1)

    elif message.text == "📙 2-sinf darsliklari":
        file2 = FSInputFile("2-sinf.pdf")
        photo2 = FSInputFile("2-sinf.webp")
        await message.answer_document(file2)
        await message.answer_photo(photo2)

    elif message.text == "📙 3-sinf darsliklari":
        file3 = FSInputFile("3-sinf.pdf")
        photo3 = FSInputFile("3-sinf.webp")
        await message.answer_document(file3)
        await message.answer_photo(photo3)

    elif message.text == "📙 4-sinf darsliklari":
        file4 = FSInputFile("4-sinf.pdf")
        photo4 = FSInputFile("4-sinf.webp")
        await message.answer_document(file4)
        await message.answer_photo(photo4)


@dp.message(F.text == "🌐 IT course")
async def reaction_to_it(message: Message):
    await message.answer(
        "Dasturlash bo'yicha qo'llanmani tanlang:",
        reply_markup=await it_buttons()
    )



@dp.message(F.text == "📘 Dasturlash bo'yicha qo'llanma")
async def reaction_to_guide(message: Message):
    fileq = FSInputFile("qollanma1.pdf")
    fileql = FSInputFile("qollanma2.pdf")

    await message.answer_document(fileq)
    await message.answer_document(fileql)


@dp.message(F.contact)
async def reaction_to_contact(message: Message):
    await message.answer(
        f"Telefon raqami: {message.contact.phone_number}"
    )


@dp.message(F.location)
async def reaction_to_location(message: Message):
    latitude = message.location.latitude
    longitude = message.location.longitude

    await message.answer(
        f"Latitude: {latitude}\nLongitude: {longitude}"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

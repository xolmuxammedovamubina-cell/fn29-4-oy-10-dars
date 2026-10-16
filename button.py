
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def main_buttons():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📚 Maktab darsliklari"),
                KeyboardButton(text="📚 Badiiy adabiyotlar")
            ],
            [
                KeyboardButton(text="🌐 IT course"),
                KeyboardButton(text="📚 IELTS course")
            ],
            [
                KeyboardButton(
                    text="Send location",
                    request_location=True
                ),
                KeyboardButton(
                    text="Send contact",
                    request_contact=True
                )
            ]
        ],
        resize_keyboard=True
    )
    return markup


async def school_buttons():
    buttons = []

    for i in range(1, 12):
        buttons.append([
            KeyboardButton(text=f"📙 {i}-sinf darsliklari")
        ])

    buttons.append([KeyboardButton(text="Go Back")])

    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )


async def it_buttons():
    buttons = [
        [
            KeyboardButton(
                text="📘 Dasturlash bo'yicha qo'llanma"
            )
        ],
        [
            KeyboardButton(text="Go Back")
        ]
    ]

    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )

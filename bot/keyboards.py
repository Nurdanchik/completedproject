from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButtonPollType
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram.exceptions import TelegramBadRequest


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Турниры'),
            KeyboardButton(text='Новости'),
            KeyboardButton(text='Наши ссылки'),
        ],
        ],resize_keyboard=True,
    # one_time_keyboard=True,
    input_field_placeholder='Выберите действие в меню',
    selective=True,
)


links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Instagram', url='https://instagram.com/nnyshanovv'),
            InlineKeyboardButton(text='GitHub', url='https://github.com/Nurdanchik/'),
        ]
    ]
)
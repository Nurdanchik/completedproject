import asyncio
from contextlib import suppress
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.enums.dice_emoji import DiceEmoji
import random
from aiogram.exceptions import TelegramBadRequest
import keyboards
import httpx
import aiohttp
from config import bot

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer(f'Hello, <b>{message.from_user.first_name}</b>', reply_markup=keyboards.main_kb)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

@dp.message()
async def echo(message:Message):
    msg = message.text.lower()

    if msg == 'турниры, новости':
         await message.answer(f'Выбирайте:', reply_markup=keyboards.spec_kb)       

    elif msg== 'наши ссылки':
        await message.answer(f'Держи:', reply_markup=keyboards.links_kb)
    
    elif msg== 'назад в меню':
        await message.answer(f'Готово:', reply_markup=keyboards.main_kb)

@dp.message()
async def tournaments(message:Message):
    msg = message.text.lower()

    if msg == 'турниры':
        to_parse_url = 'http://127.0.0.1:8000/api/tournamentslist'

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(to_parse_url) as response:
                    data = await response.json()

            for tournament in data:
                tournament_id = tournament.get('id')
                description = tournament.get('description')
                await message.answer(f"Tournament ID: {tournament_id}, Description: {description}")

        except Exception as e:
            print(f"Error fetching tournaments: {e}")

@dp.message()
async def tournaments(message:Message):
    msg = message.text.lower()

    if msg== 'новости':
        to_parse_url = 'http://127.0.0.1:8000/api/newslist'

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(to_parse_url) as response:
                    data = await response.json()

            for news_item in data:
                news_id = news_item.get('id')
                price_fund = news_item.get('price_fund')
                who_is_owner = news_item.get('whoisowner')
                price_for_participating = news_item.get('price_for_participating')
                description = news_item.get('description')

                await message.answer(f"News ID: {news_id}, Price Fund: {price_fund}, Owner: {who_is_owner}, "
                                    f"Participation Price: {price_for_participating}, Description: {description}")

        except Exception as e:
            print(f"Error fetching news: {e}")


if __name__ == '__main__':
    asyncio.run(main())



# import asyncio
# from contextlib import suppress
# from aiogram import Bot, Dispatcher, F, types
# from aiogram.filters import Command, CommandObject, CommandStart
# from aiogram.types import Message, CallbackQuery
# from aiogram.enums.dice_emoji import DiceEmoji
# import random
# from aiogram.exceptions import TelegramBadRequest
# import keyboards
# import httpx
# from config import bot

# dp = Dispatcher()

# @dp.message(CommandStart())
# async def start(message:Message):
#     await message.answer(f'Hello, <b>{message.from_user.first_name}</b>', reply_markup=keyboards.main_kb)

# async def main():
#     await bot.delete_webhook(drop_pending_updates=True)
#     await dp.start_polling(bot)

# async def get_tournaments():
#     async with httpx.AsyncClient() as client:
#         response = await client.get('http://127.0.0.1:8000/api/tournamentslist')
#         return response.json()

# async def get_news():
#     async with httpx.AsyncClient() as client:
#         response = await client.get('http://127.0.0.1:8000/api/newslist')
#         return response.json()

# @dp.message_handler(lambda message: message.text.lower() == 'турниры', content_types=['text'])
# async def tournaments(message: types.Message):
#     tournament_data = await get_tournaments()
#     if tournament_data:
#         for tournament in tournament_data:
#             await message.answer(f"{tournament['name']} - {tournament['date']}")
#     else:
#         await message.answer('Error fetching tournament data.')

# @dp.message_handler(lambda message: message.text.lower() == 'новости', content_types=['text'])
# async def news(message: types.Message):
#     news_data = await get_news()
#     if news_data:
#         for news_item in news_data:
#             await message.answer(f"{news_item['title']} - {news_item['date']}")
#     else:
#         await message.answer('Error fetching news data.')   

# @dp.message()
# async def echo(message:Message):
#     msg = message.text.lower()

#     if msg == 'информация о турнирах':
#         await message.answer(f'Наши ссылки:', reply_markup=keyboards.spec_kb)       

#     elif msg == 'наши ссылки':
#         await message.answer(f'Держи:', reply_markup=keyboards.links_kb)
    
#     elif msg == 'назад в меню':
#         await message.answer(f'Готово:', reply_markup=keyboards.main_kb)

# if __name__ == '__main__':
#     asyncio.run(main())

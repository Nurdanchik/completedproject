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

    if msg == 'турниры':
        to_parse_tournaments_url = 'http://127.0.0.1:8000/api/tournamentslist'

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(to_parse_tournaments_url) as response:
                    data = await response.json()

            for tournament in data:
                tournament_id = tournament.get('id')
                price_fund = tournament.get('price_fund')
                price_for_participating = tournament.get('price_for_participating')
                description = tournament.get('description')
                allowedteams = tournament.get('teamsallowed')
                alreadyin = tournament.get('alreadyin')
                date = tournament.get('date')
                players = tournament.get('players')
                formatt = tournament.get('formatt')

                await message.answer(f"""
                                     
ID турнира : {tournament_id}. 
Призовой фонд: {price_fund}.
Цена за участие: {price_for_participating}.
Описание: {description}
Разрешено команд: {allowedteams}
Уже участвует: {alreadyin}
Дата проведения: {date}
Количество игроков уже:{players}
Формат турнира:{formatt}

""")

        except Exception as e:
            print(f"Error fetching tournaments: {e}") 

    elif msg== 'наши ссылки':
        await message.answer(f'Держи:', reply_markup=keyboards.links_kb)

    elif msg== 'новости':
        to_parse_news_url = 'http://127.0.0.1:8000/api/newslist'

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(to_parse_news_url) as response:
                    data = await response.json()

            for news_item in data:
                news_id = news_item.get('id')
                description = news_item.get('description')
                await message.answer(f"""
                                     
ID новости: {news_id}.
Описание: {description}

""")

        except Exception as e:
            print(f"Error fetching news: {e}")
    
    elif msg== 'назад в меню':
        await message.answer(f'Готово:', reply_markup=keyboards.main_kb)


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

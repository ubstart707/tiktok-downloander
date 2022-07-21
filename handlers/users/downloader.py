from multiprocessing.connection import answer_challenge
from aiogram import types
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from loader import dp
from tiktok import tk
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CallbackQuery
@dp.message_handler(Text(startswith=['https://vt.tiktok.com/','https://www.tiktok.com/'])) 
async def test(message:types.Message):
    natija = tk(message.text)
    qoshiq = natija['music']
    print(natija)
    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Mp3 download", url="{}".format(qoshiq))]
        ]
    )
    await message.answer_audio(natija['video'], reply_markup=btn)
# @dp.callback_query_handler(Text(startswith='🎧'))
# async def test2(call:CallbackQuery):
#     await call.answer(cache_time=60)
#     data = call.data[1:]
#     await call.message.answer_audio(data)



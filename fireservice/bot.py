import logging
import os

from aiogram import Bot, Dispatcher, executor, types, utils
import menu as nav

API_TOKEN = os.getenv('TELE_TOCKEN')


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode="html")
dp = Dispatcher(bot)

media = types.MediaGroup()


# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     await message.reply("Привет!\nЯ - бот FireVision от Dragon IT и я создан для предотвращения пожаров\n Чтобы начать, нажмите /menu", nav.mainMenu)


def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton("Share Position", request_location=True)
    keyboard.add(button)
    return keyboard


@dp.message_handler(commands=['start'])
async def command_start(message:types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name}' .format(message.from_user), reply_markup = nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    # await bot.send_message(message.from_user.id, message.text)

    if message.text == 'Сообщить о возгорании':
        await bot.send_message(message.from_user.id, 'Пожалуйста, поделитесь своей геопозицией, нажав /locate_fire ', )

    elif message.text == '/locate_fire':
          reply = "Нажмите на кнопку ниже, чтобы поделиться геолокацией"
          await message.answer(reply, reply_markup=get_keyboard())

    elif message.text == '/send_photo':
       await message.input_media_photo.InputMediaPhoto()

    elif message.text == 'Пожар':
         await bot.send_message(message.from_user.id, 'Внимание! Обнаружена точка возгарания')

    

@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    await message.photo[-1].download()


@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "latitude:  {}\nlongitude: {} \nПожалуйста, направьте фото точки возгорания, нажав /send_photo".format(lat, lon)
    await message.answer(reply, reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands=['locate_fire'])
async def cmd_locate_fire(message: types.Message):
    reply = "Click on the the button below to share your location"
    await message.answer(reply, reply_markup=get_keyboard())


# async def echo(message: types.Message):
#     await message.answer(message.text)

def main():
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()


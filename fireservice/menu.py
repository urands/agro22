from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')

btnAlarm = KeyboardButton('Сообщить о возгорании')
btnCamera = KeyboardButton('Запрос камеры')
btnOther = KeyboardButton('Другое')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnAlarm, btnCamera, btnOther)

btnInfo = KeyboardButton('Информация')
btnMoney = KeyboardButton('Курсы валют')
otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnInfo, btnMoney, btnMain)


from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton('Внески', callback_data='m1')],
        [InlineKeyboardButton('Кошторис', callback_data='m2')],
        [InlineKeyboardButton('Правління ОСББ', callback_data='m3')],
        [InlineKeyboardButton('Телефонна книга ОСББ', callback_data='m4')],
    ]
    return InlineKeyboardMarkup(keyboard)


def back_to_main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Головне меню', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

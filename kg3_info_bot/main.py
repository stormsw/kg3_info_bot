from functools import wraps
from os import getenv

from telegram import (Bot, ParseMode, Update)
from telegram.ext import CommandHandler, Updater

from kg3_info_bot.common import callback_handler, send_typing_action
from kg3_info_bot.keyboards import (back_to_main_menu_keyboard,
                                    main_menu_keyboard)
from kg3_info_bot.messages import msg_reader

updater = Updater(getenv('API_KEY'), use_context=True)


@send_typing_action
def start(bot: Bot, update: Update):
    bot.message.reply_text(msg_reader(
        'main'), reply_markup=main_menu_keyboard(), parse_mode=ParseMode.MARKDOWN_V2)


@send_typing_action
@callback_handler(updater=updater, pattern='main')
def main_menu(bot: Bot, update: Update):
    bot.callback_query.message.edit_text(msg_reader(
        'main'), reply_markup=main_menu_keyboard(), parse_mode=ParseMode.MARKDOWN_V2)


@send_typing_action
@callback_handler(updater=updater, pattern='m1')
def first_menu(bot: Bot, update: Update):
    bot.callback_query.message.edit_text(msg_reader('vnesky'),
                                         reply_markup=back_to_main_menu_keyboard(),
                                         parse_mode=ParseMode.MARKDOWN_V2)


@send_typing_action
@callback_handler(updater=updater, pattern='m2')
def koshtorys_menu(bot: Bot, update: Update):
    bot.callback_query.message.edit_text(msg_reader('koshtorys'),
                                         reply_markup=back_to_main_menu_keyboard(),
                                         parse_mode=ParseMode.MARKDOWN_V2)


@send_typing_action
@callback_handler(updater=updater, pattern='m3')
def pravlinnya_menu(bot: Bot, update: Update):
    bot.callback_query.message.edit_text(msg_reader('pravlinnya'),
                                         reply_markup=back_to_main_menu_keyboard(),
                                         parse_mode=ParseMode.MARKDOWN_V2)


@send_typing_action
@callback_handler(updater=updater, pattern='m4')
def contacts_menu(bot: Bot, update: Update):
    bot.callback_query.message.edit_text(msg_reader('contacts'),
                                         reply_markup=back_to_main_menu_keyboard(),
                                         parse_mode=ParseMode.MARKDOWN_V2)


def error(update, context):
    print(f'Update {update} caused error {context.error}')


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_error_handler(error)

updater.start_polling()

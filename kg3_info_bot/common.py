from telegram.ext import Updater
from telegram.ext import CallbackQueryHandler
from telegram import ChatAction

from functools import wraps


def send_typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
        return func(update, context,  *args, **kwargs)

    return command_func

def callback_handler(updater:Updater, pattern:str):
    def decorator(func):        
        handler = CallbackQueryHandler(func, pattern=pattern)
        updater.dispatcher.add_handler(handler)
        return func
    return decorator

import threading
import logging
import telegram.error
from telegram import Update
from telegram.ext import (Updater, CommandHandler, CallbackContext)

from src.system.persistence.configApp import ConfigApp
from src.system.tracker.trackerGlobalCainiao import TrackerGlobalCainiao


def command_aliexpress(update: Update, context: CallbackContext) -> None:
    print(update.effective_user.language_code)
    print(update.effective_user.username)
    print(update.effective_user.id)
    track_order: str = context.args[0]
    if not track_order:
        update.message.reply_text('No se ha indicado el código de seguimiento')

    tracker = TrackerGlobalCainiao(track_order)
    tracker.search_track_order()
    update.message.reply_text(tracker.get_head_detail())
    update.message.reply_text(tracker.get_text_detail())
    update.message.reply_text(tracker.get_time_detail())


class TelegramBot:

    __updater: Updater

    def __init__(self):
        try:
            self.__updater = ConfigApp().get_telegram_updater()
            thread = threading.Thread(target=self.__load_bot, name='DaemonTelegramBot')
            thread.start()
        except telegram.error.InvalidToken:
            logging.info('No se ha establecido un Token válido para Telegram')

    def __load_bot(self) -> None:
        self.__updater.dispatcher.add_handler(CommandHandler('aliexpress', command_aliexpress))

        self.__updater.start_polling()
        self.__updater.idle()

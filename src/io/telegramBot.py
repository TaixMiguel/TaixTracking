import threading
import logging
import telegram.error
from telegram import Update, ForceReply
from telegram.ext import (Updater, CommandHandler, CallbackContext)

from src.system import create_user, errors, is_user, invoke_daemon
from src.system.configApp import ConfigApp
from src.system.tracker.trackerGlobalCainiao import TrackerGlobalCainiao
from src.system.tracker.trackerGlobalCainiao import TYPE as TYPE_CAINIAO
from src.system.tracker.tracking import Tracking
from src.system.tracker import create_tracking


def __get_user_id(update: Update) -> int:
    return update.effective_user.id


def __get_user_nick(update: Update) -> str:
    return update.effective_user.username


def __get_user_language_code(update: Update) -> str:
    return update.effective_user.language_code


def __check_user(update: Update) -> bool:
    if not is_user(__get_user_id(update)):
        if ConfigApp().is_allow_new_users():
            create_user(__get_user_id(update), __get_user_nick(update), __get_user_language_code(update))
            return True
        logging.info(f'El usuario de Telegram "{__get_user_nick(update)}" se ha puesto en contacto conmigo')
        update.message.reply_text('No atiendo peticiones de desconocidos')
        raise Exception("Usuario no registrado")
        return False
    return True


def command_aliexpress(update: Update, context: CallbackContext) -> None:
    __check_user(update)
    track_order: str = context.args[0]
    if not track_order:
        update.message.reply_text('No se ha indicado el código de seguimiento')

    try:
        create_tracking(TYPE_CAINIAO, track_order, __get_user_id(update))
        update.message.reply_text('Es posible que tardes un rato en recibir una respuesta. Por favor, sé paciente.')
    except errors.IntegrityError:
        update.message.reply_text('No se puede dar de alta un tracking ya existente.')
    invoke_daemon()
    # TODO: pedir el alias del pedido
    # TODO: pedir la fecha de vencimiento


class TelegramBot:

    __updater: Updater

    def __init__(self):
        try:
            self.__updater = ConfigApp().get_telegram_updater()
            self.__set_commands()

            self.__updater.start_polling()
            self.__updater.idle()
        except telegram.error.InvalidToken:
            logging.info('No se ha establecido un Token válido para Telegram')

    def __set_commands(self) -> None:
        self.__updater.dispatcher.add_handler(CommandHandler('aliexpress', command_aliexpress))

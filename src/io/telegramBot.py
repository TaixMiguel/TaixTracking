import logging
import telegram.error
from telegram import Bot, Update, ForceReply
from telegram.ext import (Updater, CommandHandler, CallbackContext)

from src import constant
from src.io.abstractCommunication import AbstractCommunication
from src.system import create_user, errors, is_user_telegram, get_user, get_user_telegram
from src.system.user import User
from src.system.configApp import ConfigApp
from src.system.tracker.trackerGlobalCainiao import TYPE as TYPE_CAINIAO
from src.system.tracker import create_tracking


def __get_user_id(update: Update) -> int:
    return update.effective_user.id


def __get_user_nick(update: Update) -> str:
    return update.effective_user.username


def __get_user_language_code(update: Update) -> str:
    return update.effective_user.language_code


def __check_user(update: Update) -> User:
    if not is_user_telegram(__get_user_id(update)):
        if ConfigApp().is_allow_new_users():
            return create_user(__get_user_id(update), __get_user_nick(update), __get_user_language_code(update))
        logging.info(f'El usuario de Telegram "{__get_user_nick(update)}" se ha puesto en contacto conmigo')
        update.message.reply_text('No atiendo peticiones de desconocidos')
        raise Exception("Usuario no registrado")
        return None
    return get_user_telegram(telegram_id=__get_user_id(update))


def command_aliexpress(update: Update, context: CallbackContext) -> None:
    user: User = __check_user(update)
    track_order: str = context.args[0]
    if not track_order:
        update.message.reply_text('No se ha indicado el código de seguimiento')

    try:
        # TODO: comprobar si el tracking existe en otro usuario
        create_tracking(TYPE_CAINIAO, track_order, user.get_id())
        update.message.reply_text('Es posible que tardes un rato en recibir una respuesta. Por favor, sé paciente.')
    except errors.IntegrityError:
        update.message.reply_text('No se puede dar de alta un tracking ya existente.')
    # TODO: pedir el alias del pedido
    # TODO: pedir la fecha de vencimiento


class TelegramBot(AbstractCommunication):

    __updater: Updater

    def __init__(self):
        try:
            self.__updater = ConfigApp().get_telegram_updater()
        except telegram.error.InvalidToken:
            logging.info('No se ha establecido un Token válido para Telegram')

    def run(self) -> None:
        self.__set_commands()
        self.__updater.start_polling()
        self.__updater.idle()

    def send_message(self, id_user: int, msg: str) -> None:
        user: User = get_user(id_user)
        if user:
            id_telegram: int = user.get_value_attribute(constant.AttributeUser.TELEGRAM_USER_ID)
            if id_telegram:
                self.__updater.bot.send_message(chat_id=id_telegram, text=msg)

    def __set_commands(self) -> None:
        self.__updater.dispatcher.add_handler(CommandHandler('aliexpress', command_aliexpress))

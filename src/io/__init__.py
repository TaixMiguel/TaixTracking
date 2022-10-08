from src.io.abstractCommunication import AbstractCommunication
from src.io.telegramBot import TelegramBot


def get_instance_communication() -> AbstractCommunication:
    return TelegramBot()

import json
import logging
import os

from telegram.ext import Updater
from threading import Lock


class ConfigAppMeta(type):

    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class ConfigApp(metaclass=ConfigAppMeta):

    __configData: dict = {}

    def __init__(self) -> None:
        path_file: str
        try:
            path_file = os.environ['CONFIG_FILE_TAIXTRACKING']
            with open(path_file, 'r') as config_file:
                self.__configData = json.load(config_file)
        except KeyError:
            logging.error('No se ha definido la variable de entorno CONFIG_FILE_TAIXTRACKING')
            logging.info('Se detiene la ejecución de la aplicación')
            quit()
        except FileNotFoundError:
            logging.error(f'No se encuentra el fichero de configuración "{path_file}"')
            logging.info('Se detiene la ejecución de la aplicación')
            quit()

    def get_telegram_updater(self) -> Updater:
        return Updater(self.__configData['telegram']['token'], arbitrary_callback_data=True)

    def is_allow_new_users(self) -> bool:
        try:
            return self.__configData['application']['users']['allow_new_users']
        except KeyError:
            return False

    def is_allow_user(self) -> bool:
        try:
            return self.__configData['application']['users']['default_allow']
        except KeyError:
            return False

    def get_database_system(self) -> str:
        try:
            return self.__configData['bbdd']['system']
        except KeyError:
            return 'sqlite'

    def get_database_filepath(self) -> str:
        try:
            return self.__configData['bbdd']['filepath']
        except KeyError:
            return 'taixTracking.db'

import logging
from src.system.configApp import ConfigApp
from src.system.persistence.bbdd import get_instance as get_instance_bbdd
from src.system.user import User, to_users


def is_user(telegram_id: int) -> bool:
    database_manager = get_instance_bbdd()
    rows: list = database_manager.select('suser001', [telegram_id])
    database_manager.close()
    return True if rows else False


def get_user(user_id: int) -> User:
    database_manager = get_instance_bbdd()
    rows: list = database_manager.select('suser002', [user_id])
    database_manager.close()
    if rows:
        return to_users(rows)[0]
    return None


def get_user_telegram(telegram_id: int) -> User:
    database_manager = get_instance_bbdd()
    rows: list = database_manager.select('suser001', [telegram_id])
    database_manager.close()
    if rows:
        return to_users(rows)[0]
    return None


def create_user(telegram_id: int, telegram_username: str, telegram_language_code: str) -> User:
    logging.debug(f'Se crea el usuario "{telegram_username}"')
    database_manager = get_instance_bbdd()
    database_manager.insert('iuser001', [telegram_id, telegram_username, telegram_language_code,
                                         ConfigApp().is_allow_user()])
    database_manager.close()
    return get_user_telegram(telegram_id=telegram_id)

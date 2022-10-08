import logging

from src import constant
from src.system.configApp import ConfigApp
from src.system.persistence.bbdd import get_instance as get_instance_bbdd
from src.system.user import User, to_users


def is_user_telegram(telegram_id: int) -> bool:
    database_manager = get_instance_bbdd()
    rows: list = database_manager.select('suser002', [constant.AttributeUser.TELEGRAM_USER_ID, telegram_id])
    database_manager.close()
    return True if rows else False


def get_user(user_id: int) -> User:
    database_manager = get_instance_bbdd()
    rows: list = database_manager.select('suser001', [user_id])
    database_manager.close()
    if rows:
        return to_users(rows)[0]
    return None


def get_user_by_attribute(attribute_key: str, attribute_value: str) -> User:
    database_manager = get_instance_bbdd()
    rows: list = database_manager.select('suser002', [attribute_key, attribute_value])
    database_manager.close()
    if rows:
        return get_user(rows[0][0])
    return None


def get_user_telegram(telegram_id: int) -> User:
    return get_user_by_attribute(constant.AttributeUser.TELEGRAM_USER_ID, telegram_id)


def _create_user_attribute(database_manager, id_user: int, attribute_key: str, attribute_value: str) -> None:
    database_manager.insert('iuser002', [id_user, attribute_key, attribute_value])


def create_user(telegram_id: int, telegram_username: str, telegram_language_code: str) -> User:
    logging.debug(f'Se crea el usuario "{telegram_username}"')
    database_manager = get_instance_bbdd()
    id_user: int = database_manager.insert('iuser001', [ConfigApp().is_allow_user()])
    _create_user_attribute(database_manager, id_user, constant.AttributeUser.TELEGRAM_USER_ID, telegram_id)
    _create_user_attribute(database_manager, id_user, constant.AttributeUser.TELEGRAM_USER_NAME, telegram_username)
    _create_user_attribute(database_manager, id_user, constant.AttributeUser.TELEGRAM_USER_LANGUAGE,
                           telegram_language_code)
    database_manager.close()
    return get_user(id_user)

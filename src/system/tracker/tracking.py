from src.system.persistence.bbdd import get_instance as get_instance_bbdd
import logging


def to_tracking(rows: list) -> list:
    trackers: list = []
    for row in rows:
        trackers.append(Tracking(row))
    return trackers


def get_instances_by_telegram_user(telegram_user_id: int) -> list:
    database_manager = get_instance_bbdd()
    rows: list = database_manager.select('strack002', [telegram_user_id])
    database_manager.close()
    return to_tracking(rows)


class Tracking:

    __id: int
    __track_type: str
    __track_code: str
    __telegram_user_id: int
    __track_alias: str
    __expiration_date: int
    __last_update: int
    __creation_time: int
    __audit_time: int

    def __init__(self, row: tuple):
        self.__id = row[0]
        self.__track_type = row[1]
        self.__track_code = row[2]
        self.__telegram_user_id = row[3]
        self.__track_alias = row[4]
        self.__expiration_date = row[5]
        self.__last_update = row[6]
        self.__creation_time = row[7]
        self.__audit_time = row[8]

    def update_alias(self, track_alias: str) -> bool:
        logging.debug(f'Se actualiza el alias del track "{self.__track_type}: {self.__track_code}"')
        database_manager = get_instance_bbdd()
        database_manager.insert('utrack001', [track_alias, self.__id])
        self.__track_alias = track_alias
        database_manager.close()
        return True

    def update_expiration_date(self, expiration_date: int) -> bool:
        logging.debug(f'Se actualiza la fecha de vencimiento del track "{self.__track_type}: {self.__track_code}"')
        database_manager = get_instance_bbdd()
        database_manager.insert('utrack002', [expiration_date, self.__id])
        self.__expiration_date = expiration_date
        database_manager.close()
        return True

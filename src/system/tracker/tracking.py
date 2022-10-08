from src.system.persistence.bbdd import get_instance as get_instance_bbdd
from src.system.tracker.trackingDetail import TrackingDetail, to_tracking_detail
import logging


def to_tracking(rows: list) -> list:
    trackers: list = []
    for row in rows:
        trackers.append(Tracking(row))
    return trackers


def get_actives_tracking() -> list:
    database_manager = get_instance_bbdd()
    rows: list = database_manager.select('strack002', [])
    database_manager.close()
    return to_tracking(rows)


class TrackingUser:

    __id: int
    __id_user_fk: int
    __id_tracking_fk: int
    __track_alias: str

    def __init__(self, row: tuple):
        self.__id = row[0]
        self.__id_user_fk = row[1]
        self.__id_tracking_fk = row[2]
        self.__track_alias = row[3]

    def get_id(self) -> int:
        return self.__id

    def get_id_user_fk(self) -> int:
        return self.__id_user_fk

    def get_id_tracking_fk(self) -> int:
        return self.__id_tracking_fk

    def get_alias(self) -> str:
        return self.__track_alias

    def update_alias(self, track_alias: str) -> bool:
        self.__track_alias = track_alias
        database_manager = get_instance_bbdd()
        database_manager.insert('utrack001', [track_alias, self.__id_user_fk, self.__id_tracking_fk])
        database_manager.close()
        return True


class Tracking:

    __id: int
    __track_type: str
    __track_code: str
    __user_id: int
    __track_alias: str
    __expiration_date: int
    __last_update: int
    __creation_time: int
    __audit_time: int

    __tracking_users: dict

    def __init__(self, row: tuple):
        self.__id = row[0]
        self.__track_type = row[1]
        self.__track_code = row[2]
        self.__expiration_date = row[3]
        self.__last_update = row[4]
        self.__creation_time = row[5]
        self.__audit_time = row[6]
        self.__tracking_users = {}

        database_manager = get_instance_bbdd()
        tracking_users_rows: list = database_manager.select('strack004', [self.__id])
        database_manager.close()

        for tracking_user_rows in tracking_users_rows:
            tracking_user: TrackingUser = TrackingUser(tracking_user_rows)
            self.__tracking_users[tracking_user.get_id_user_fk()] = tracking_user

    def get_id(self) -> int:
        return self.__id

    def get_track_type(self) -> str:
        return self.__track_type

    def get_track_code(self) -> str:
        return self.__track_code

    def get_ids_user(self) -> list:
        ids_user: list = []
        for tracking_user in self.__tracking_users:
            ids_user.append(tracking_user)
        return ids_user

    def get_track_alias(self, id_user: int) -> str:
        return self.__get_tracking_user(id_user).get_alias()

    def get_expiration_date(self) -> int:
        return self.__expiration_date

    def get_last_update(self) -> int:
        return self.__last_update

    def get_creation_time(self) -> int:
        return self.__creation_time

    def get_audit_time(self) -> int:
        return self.__audit_time

    def __get_tracking_user(self, id_user: int) -> TrackingUser:
        return self.__tracking_users[id_user]

    def update_alias(self, id_user: int, track_alias: str) -> bool:
        return self.__get_tracking_user(id_user).update_alias(track_alias)

    def update_expiration_date(self, expiration_date: int) -> bool:
        logging.debug(f'Se actualiza la fecha de vencimiento del track "{self.to_string()}"')
        database_manager = get_instance_bbdd()
        database_manager.insert('utrack002', [expiration_date, self.__id])
        self.__expiration_date = expiration_date
        database_manager.close()
        return True

    def get_last_detail(self) -> TrackingDetail:
        database_manager = get_instance_bbdd()
        rows: list = database_manager.select('strack003', [self.__id])
        database_manager.close()
        if not rows:
            return None
        return to_tracking_detail(rows)[len(rows)-1]

    def create_new_tracking_detail(self, head: str, text: str, time: int) -> TrackingDetail:
        database_manager = get_instance_bbdd()
        database_manager.insert('itrack002', [self.__id, head, text, time])
        database_manager.close()

        # TODO: avisar al usuario del nuevo detalle encontrado
        return self.get_last_detail()

    def to_string(self) -> str:
        return self.__track_type + ': ' + self.__track_code

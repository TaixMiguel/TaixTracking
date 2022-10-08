def to_users(rows: list) -> list:
    users: list = []
    for row in rows:
        users.append(User(row))
    return users


class User:

    __id: int
    __telegram_id: int
    __telegram_username: str
    __telegram_language_code: str
    __sw_allow: bool
    __creation_time: int
    __audit_time: int

    def __init__(self, row: tuple):
        self.__id = row[0]
        self.__telegram_id = row[1]
        self.__telegram_username = row[2]
        self.__telegram_language_code = row[3]
        self.__sw_allow = row[4]
        self.__creation_time = row[5]
        self.__audit_time = row[6]

    def get_id(self) -> int:
        return self.__id

    # TODO: sacar a una tabla de atributos
    def get_telegram_id(self) -> int:
        return self.__telegram_id

    # TODO: sacar a una tabla de atributos
    def get_telegram_username(self) -> str:
        return self.__telegram_username

    # TODO: sacar a una tabla de atributos
    def get_telegram_language(self) -> str:
        return self.__telegram_language_code

    def is_allow(self) -> bool:
        return self.__sw_allow

    def get_creation_time(self) -> int:
        return self.__creation_time

    def get_audit_time(self) -> int:
        return self.__audit_time

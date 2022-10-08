from src.system.persistence.bbdd import get_instance as get_instance_bbdd


def to_users(rows: list) -> list:
    users: list = []
    for row in rows:
        users.append(User(row))
    return users


class UserAttr:

    __id: int
    __id_user_fk: int
    __attribute_key: str
    __attribute_value: str

    def __init__(self, row: tuple):
        self.__id = row[0]
        self.__id_user_fk = row[1]
        self.__attribute_key = row[2]
        self.__attribute_value = row[3]

    def get_id(self) -> int:
        return self.__id

    def get_id_user(self) -> int:
        return self.__id_user_fk

    def get_key(self) -> str:
        return self.__attribute_key

    def get_value(self) -> str:
        return self.__attribute_value


class User:

    __id: int
    __sw_allow: bool
    __creation_time: int
    __audit_time: int

    __attributes: dict

    def __init__(self, row: tuple):
        self.__id = row[0]
        self.__sw_allow = row[1]
        self.__creation_time = row[2]
        self.__audit_time = row[3]
        self.__attributes = {}

        database_manager = get_instance_bbdd()
        attrs_rows: list = database_manager.select('suser003', [self.__id])
        database_manager.close()

        for attr_rows in attrs_rows:
            attribute: UserAttr = UserAttr(attr_rows)
            self.__attributes[attribute.get_key()] = attribute

    def get_id(self) -> int:
        return self.__id

    def is_allow(self) -> bool:
        return self.__sw_allow

    def get_creation_time(self) -> int:
        return self.__creation_time

    def get_audit_time(self) -> int:
        return self.__audit_time

    def get_attribute(self, attribute: str) -> UserAttr:
        return self.__attributes[attribute]

    def get_value_attribute(self, attribute: str) -> str:
        user_attribute: UserAttr = self.get_attribute(attribute)
        if user_attribute:
            return user_attribute.get_value()
        return ''

import sqlite3
from sqlite3 import Connection, Error
from src.system.persistence.bbdd.abstractDatabaseManager import read_sql_file
from src.system.persistence.bbdd.abstractDatabaseManager import AbstractDatabaseManager

SYSTEM = 'sqlite'
__PATH_TABLES = 'resources/bbdd/sqlite/tables/'
__PATH_SCRIPTS = 'resources/bbdd/sqlite/scripts/'


def create_table(cursor, table: str) -> None:
    sql: str = read_sql_file(__PATH_TABLES + table + '.sql')
    try:
        cursor.execute(sql)
    except Error as e:
        print(e)


class ManagerSQLite(AbstractDatabaseManager):

    __connection: Connection

    def __init__(self, database: str):
        super().__init__(database)

    def _create_connection(self, database: str) -> None:
        self.__connection = sqlite3.connect(database)

    def commit(self) -> None:
        self.__connection.commit()

    def rollback(self) -> None:
        self.__connection.rollback()

    def _create_tables(self, tables: list) -> None:
        cursor = self.__connection.cursor()
        list(map(lambda table: create_table(cursor, table), tables))

    def close(self) -> None:
        self.__connection.close()

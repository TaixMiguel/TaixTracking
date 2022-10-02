import sqlite3
from sqlite3 import Connection, Cursor, Error
from src.system import errors
from src.system.persistence.bbdd.abstractDatabaseManager import read_sql_file
from src.system.persistence.bbdd.abstractDatabaseManager import AbstractDatabaseManager

SYSTEM = 'sqlite'
_PATH_TABLES = 'resources/bbdd/sqlite/tables/'
_PATH_SCRIPTS = 'resources/bbdd/sqlite/scripts/'


def create_table(cursor, table: str) -> None:
    sql: str = read_sql_file(_PATH_TABLES + table + '.sql')
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

    def _create_tables(self, tables: list) -> None:
        cursor: Cursor = self.__connection.cursor()
        list(map(lambda table: create_table(cursor, table), tables))

    def __execute(self, script: str, params) -> int:
        sql: str = read_sql_file(_PATH_SCRIPTS + script + '.sql')
        cursor: Cursor = self.__connection.cursor()
        cursor.execute(sql, params)
        return cursor.lastrowid

    def _insert(self, script: str, params) -> int:
        try:
            return self.__execute(script, params)
        except sqlite3.IntegrityError as error:
            raise errors.IntegrityError(error)

    def _select(self, script: str, params) -> list:
        sql: str = read_sql_file(_PATH_SCRIPTS + script + '.sql')
        cursor: Cursor = self.__connection.cursor()
        cursor.execute(sql, params)
        return cursor.fetchall()

    def _update(self, script: str, params) -> int:
        return self.__execute(script, params)

    def _commit(self) -> None:
        self.__connection.commit()

    def _rollback(self) -> None:
        self.__connection.rollback()

    def close(self) -> None:
        self.__connection.close()

from abc import ABC, abstractmethod
import logging


def read_sql_file(sql_file: str) -> str:
    try:
        with open(sql_file, encoding='utf8') as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f'No se encuentra la sql "{sql_file}"')


class AbstractDatabaseManager(ABC):

    def __init__(self, database: str):
        self._create_connection(database)

    @abstractmethod
    def _create_connection(self, database: str) -> None:
        pass

    def create_application_tables(self) -> None:
        tables: list = ['trackingDetails', 'trackings', 'users', 'userAttributes']
        self._create_tables(tables)

    @abstractmethod
    def _create_tables(self, tables: list) -> None:
        pass

    def insert(self, sql: str, params) -> int:
        try:
            row_id: int = self._insert(sql, params)
            self._commit()
            return row_id
        except Exception as error:
            self._rollback()
            logging.exception(error)
            raise error

    @abstractmethod
    def _insert(self, script: str, params) -> int:
        pass

    def select(self, sql: str, params) -> list:
        try:
            return self._select(sql, params)
        except Exception as error:
            logging.exception(error)
            raise error

    @abstractmethod
    def _select(self, script: str, params) -> list:
        pass

    def update(self, sql: str, params) -> int:
        try:
            row_id: int = self._update(sql, params)
            self._commit()
            return row_id
        except Exception as error:
            self._rollback()
            logging.exception(error)

    @abstractmethod
    def _update(self, script: str, params) -> int:
        pass

    @abstractmethod
    def _commit(self) -> None:
        pass

    @abstractmethod
    def _rollback(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

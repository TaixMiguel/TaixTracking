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

    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def rollback(self) -> None:
        pass

    def create_application_tables(self) -> None:
        tables: list = ['trackingDetails', 'trackings', 'users']
        self._create_tables(tables)

    @abstractmethod
    def _create_tables(self, tables: list) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

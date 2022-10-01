from src.system.configApp import ConfigApp
from src.system.persistence.bbdd import managerSQLite
from src.system.persistence.bbdd.managerSQLite import ManagerSQLite
from src.system.persistence.bbdd.abstractDatabaseManager import AbstractDatabaseManager


def get_instance() -> AbstractDatabaseManager:
    config_app: ConfigApp = ConfigApp()
    system: str = config_app.get_database_system()

    if system == managerSQLite.SYSTEM:
        return ManagerSQLite(config_app.get_database_filepath())

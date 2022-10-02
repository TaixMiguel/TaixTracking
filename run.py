from src.io.telegramBot import TelegramBot
from src.system import invoke_daemon
from src.system.persistence.bbdd import get_instance as get_instance_bbdd
from src.system.persistence.bbdd.abstractDatabaseManager import AbstractDatabaseManager

if __name__ == '__main__':
    database_manager: AbstractDatabaseManager = get_instance_bbdd()
    database_manager.create_application_tables()
    database_manager.close()

    invoke_daemon()
    TelegramBot()

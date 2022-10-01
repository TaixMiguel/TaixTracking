from src.io.telegramBot import TelegramBot
from src.system.persistence.bbdd import get_instance as get_instance_bbdd

if __name__ == '__main__':
    database_manager = get_instance_bbdd()
    database_manager.create_application_tables()
    database_manager.close()

    TelegramBot()

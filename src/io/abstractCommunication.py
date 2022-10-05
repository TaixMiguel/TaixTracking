from abc import ABC, abstractmethod


class AbstractCommunication(ABC):

    @abstractmethod
    def send_message(self, id_user: int, msg: str) -> None:
        pass

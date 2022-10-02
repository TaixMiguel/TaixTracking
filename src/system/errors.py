class IntegrityError(Exception):
    __error: Exception

    def __init__(self, error: Exception):
        self.__error = error

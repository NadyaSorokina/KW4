class ErrorResponse(Exception):
    """ Исключение ошибки при подключении"""
    def __init__(self, message = None):
        super().__init__(message)


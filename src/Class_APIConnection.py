from abc import ABC, abstractmethod
import requests
from src.exception import ErrorResponse


class APIIntegration(ABC):
    """ Абстрактный класс для проверки подключения по API"""


    def __init__(self):
        self.request_result = False


    @abstractmethod
    def response_check(self):
        """Проверка подключения"""
        pass


class HHIntegration(APIIntegration):
    """ Класс для проверки подключения по API HH.ru"""


    def __init__(self):
        super().__init__()
        self.url = 'https://api.hh.ru/vacancies'


    def response_check(self):
        """Проверка подключения по API HH.ru"""
        response = requests.get(self.url)
        #Вызываем исключение ошибки при подключении
        try:
            if response.status_code != 200:
                raise ErrorResponse(f"Ошибка подключения {response.status_code}. Подключение не произведено")
        except ErrorResponse as e:
            self.request_result = False
            return str(e)
        else:
            self.request_result = True
            return f"Подключение произведено. Формируем список вакансий."


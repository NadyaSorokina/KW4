import json
from abc import ABC, abstractmethod


class ListModification(ABC):
    """Абстрактный класс для обработки списка вакансий"""


    @abstractmethod
    def modification_list(self):
        pass


class JsonToList(ListModification):
    """Класс формирования списка из JSON файла для обработки"""


    def __init__(self, path):
        """Конструктор класса"""
        self.path = path


    def modification_list(self):
        """Метод формирования списка из JSON файла для обработки"""
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                vacancy_list = json.load(file)
            return vacancy_list
        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON: {e})")


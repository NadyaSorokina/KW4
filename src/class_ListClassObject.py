from abc import ABC, abstractmethod
from src.Class_Vacancy import Vacancy


class ListClassObject(ABC):
    """Класс для работы со списком с объектами класса"""

    list_object: list


    def __init__(self):
        """Конструктор абстрактного класса ListClassObject"""

        self.list_object = []


    @abstractmethod
    def add_new_object(self, new_object):
        """Абстрактный метод наполнения списка объектами класса"""
        pass


class ListVacancyObject(ListClassObject):
    """Класс работы со списком объектов класса Vacancy"""


    def add_new_object(self, new_object):
        """Метод добавления в список объекта класса Vacancy"""
        if isinstance(new_object, Vacancy):
            self.list_object.append(new_object)
        else:
            raise TypeError("Можно добавить только объекты класса Vacancy")


    def create_list_class_object(self, list_info):
         """Метод создания списка объектов класса Vacancy """
         for element in list_info:
            new_vacancy = Vacancy.new_vacancy(element.get("name"), element.get("alternate_url"))
            new_vacancy.salary = element.get("salary")
            new_vacancy.requirement = element.get("snippet")
            new_vacancy.experience = element.get("experience")
            new_vacancy.employment = element.get("employment")
            self.add_new_object(new_vacancy)

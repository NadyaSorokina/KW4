from abc import ABC, abstractmethod
from src.Class_Vacancy import Vacancy


class ListClassObject(ABC):
    """Класс для работы со списком с объектами класса"""
    list_info: list
    list_object: list


    def __init__(self, list_info):
        """Конструктор абстрактного класса ListClassObject"""
        self.list_info = list_info
        self.list_object = []


    @abstractmethod
    def add_new_object(self, new_object):
        """Абстрактный метод наполнения списка объектами класса"""
        pass


class ListVacancyObject(ListClassObject):
    """Класс работы со списком объектов класса Vacancy"""


    def __init__(self, list_info: list):
        """Конструктор класса ListVacancyObject"""
        super().__init__(list_info)
        self.list_select = []
        self.list_sort = []


    def add_new_object(self, new_object):
        """Метод добавления в список объекта класса Vacancy"""
        if isinstance(new_object, Vacancy):
            self.list_object.append(new_object)
        else:
            raise TypeError("Можно добавить только объекты класса Vacancy")


    def create_list_class_object(self):
         """Метод создания списка объектов класса Vacancy """
         for element in self.list_info:
            new_vacancy = Vacancy.new_vacancy(element)
            self.add_new_object(new_vacancy)


    def  select_list_requirement(self, user_request: str):
        """Метод выборки объектов класса по свойству требований к вакансии
        из списка по запросу пользователя"""
        list_user_request = user_request.split()
        for element in self.list_object:
            count_entry = 0
            for request_element in list_user_request:
                if request_element.lower() in element.requirement.lower():
                    count_entry += 1
            if count_entry > 0:
                self.list_select.append(element)
            else:
                continue


    def sort_lists_salary(self):
        """Метод сортировки с писка с объектами класса Vacancy"""
        self.list_sort = sorted(self.list_select,
                                key=lambda item: (item['salary_to'], item['salary_from']),
                                reverse=True)
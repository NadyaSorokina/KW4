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


class ListToValidateList(ListModification):
    """Класс преобразования списка в список с необходимыми для создания
    класса Vacancy валидированными данными
    """
    vacancy_list: list


    def __init__(self, vacancy_list: list):
        """Конструктор класса ListToList"""
        self.vacancy_list = vacancy_list


    def modification_list(self):
        """Метод преобразования списка словарей, загруженного из JSON файла
        в список словарей с нужными для создания объектов класса Vacancy данными
        """
        vacancy_list_modification = []
        for vacancy in self.vacancy_list:
            vacancy_dict = {'name': vacancy.get('name'), 'url': vacancy.get("alternate_url")}
            if vacancy.get('salary') is None:
                vacancy_dict['salary_from'] = 0
                vacancy_dict["salary_to"] = 0
            else:
                if vacancy['salary'].get('from') is None:
                    vacancy_dict['salary_from'] = 0
                else:
                    vacancy_dict['salary_from'] = vacancy['salary']['from']
                if vacancy ['salary'].get('to') is None:
                    vacancy_dict["salary_to"] = 0
                else:
                    vacancy_dict["salary_to"] = vacancy["salary"]["to"]
            if vacancy.get("snippet") is None:
                vacancy_dict["requirement"] = "Требования не описаны"
            else:
                if vacancy["snippet"].get("requirement") is None:
                    vacancy_dict["requirement"] = "Требования не описаны"
                else:
                    vacancy_dict["requirement"] = (vacancy["snippet"]["requirement"].
                                                   replace("<highlighttext>", "").replace("</highlighttext>", ""))
            if vacancy.get("experience") is None:
                vacancy_dict["experience"] = "Требуемый опыт не указан"
            else:
                if vacancy["experience"].get("name") is None:
                    vacancy_dict["experience"] = "Требуемый опыт не указан"
                else:
                    vacancy_dict["experience"] = vacancy["experience"]["name"]
            if vacancy.get("employment") is None:
                vacancy_dict["employment"] = "Тип занятости не указан"
            else:
                if vacancy["employment"].get("name") is None:
                    vacancy_dict["employment"] = "Тип занятости не указан"
                else:
                    vacancy_dict["employment"] = vacancy["employment"]["name"]
            vacancy_list_modification.append(vacancy_dict)
        return vacancy_list_modification


class SortList(ListModification):
    """Класс сортировки списка валидированными данными
    для создания объектов класса Vacancy
    """
    vacancy_list: list


    def __init__(self, vacancy_list: list):
        """Конструктор класса SortList"""
        self.vacancy_list = vacancy_list


    def modification_list(self):
        """Метод сортировки списка с вакансиями"""
        sort_list_vacancy = sorted(self.vacancy_list, key=lambda item: (item['salary_to'], item['salary_from']), reverse=True)
        return sort_list_vacancy


class CropList(ListModification):
    """Класс обрезки списка"""
    vacancy_list: list
    vacancy_count: str
    def __init__(self, vacancy_list: list, vacancy_count: str):
        self.vacancy_list = vacancy_list
        self.vacancy_count = vacancy_count


    def modification_list(self):
        """Метод обрезки списка по длине, инициализированной
        в объекте класса"""
        vacancy_crop_list = self.vacancy_list.copy()
        return vacancy_crop_list[:int(self.vacancy_count)]


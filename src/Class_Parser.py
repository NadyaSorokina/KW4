import json
from abc import ABC, abstractmethod
import requests
from src.config import VACANCY_PATH


class Parser(ABC):
    """Абстрактный класс для работы с API"""


    @abstractmethod
    def load_vacancies(self, keyword):
        """
       Абстрактный метод загрузки данных
        """
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """


    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []


    def load_vacancies(self, keyword):
        """Загрузка данных по параметру"""
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1


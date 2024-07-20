import json
from abc import ABC, abstractmethod


class LoadRequests(ABC):
    """Абстрактный класс для обработки запроса"""
    def __init__(self, content_request):
        """Конструктор абстрактного класса"""
        self.content_request = content_request


    @abstractmethod
    def write_requests(self):
        """Абстрактный метод записывает полученные в запросе данные"""
        pass


class JsonLoadRequests(LoadRequests):


    def __init__(self,content_request, path):
        """Конструктор класса загрузки в JSON файл"""
        super().__init__(content_request)
        self.path = path


    def write_requests(self):
        """Метод записи в JSON файл данных, полученных из запроса"""
        with open(self.path, 'w', encoding="utf-8") as file:
            json.dump(self.content_request, file,  ensure_ascii=False, indent=4)


    def clear_json(self):
        """Метод очистки JSON файла"""
        open(self.path, "w").close()


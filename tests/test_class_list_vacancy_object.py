from src.Class_ListModification import JsonToList
from src.class_ListClassObject import ListVacancyObject
from src.config import VACANCY_PATH


def test_add_new_object(list_vacancy_class, third_vacancy):
    """Тестирование метода добавления нового объекта класса Vacancy в список"""
    list_vacancy_object = ListVacancyObject()
    list_vacancy_object.add_new_object(third_vacancy)
    assert list_vacancy_object.list_object[0].name == "Специалист по стратегии и развитию"
    assert list_vacancy_object.list_object[0].url == "https://hh.ru/vacancy/104170033"



def test_create_list_class_object():
    """Тестирование метода создания списка объектов класса Vacancy"""
    vacancy_list = JsonToList(VACANCY_PATH).modification_list()
    list_class_vacancy = ListVacancyObject()
    list_class_vacancy.create_list_class_object(vacancy_list)
    assert list_class_vacancy.list_object[0].name == "Инженер по нагрузочному тестированию junior"
    assert list_class_vacancy.list_object[0].salary == [0, 80000, "RUR", False]
    assert list_class_vacancy.list_object[2].name == "SRE инженер"
    assert list_class_vacancy.list_object[2].salary == [0]


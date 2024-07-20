from src.Class_Vacancy import Vacancy
from src.class_ListClassObject import ListVacancyObject


def test_add_new_object(list_dict_vacancy, third_vacancy):
    """Тестирование метода добавления нового объекта класса Vacancy в список"""
    list_vacancy_object = ListVacancyObject(list_dict_vacancy)
    list_vacancy_object.add_new_object(third_vacancy)
    assert list_vacancy_object.list_object[-1].name == "Специалист по стратегии и развитию"
    assert list_vacancy_object.list_object[-1].url == "https://hh.ru/vacancy/104170033"
    assert list_vacancy_object.list_object[-1].salary_from == 0
    assert list_vacancy_object.list_object[-1].salary_to == 0
    assert list_vacancy_object.list_object[-1].requirement == ("Актуализация стратегий Клуба (коммерческой стратегии, спортивной стратегии, "
                                                               "стратегий других отдельных направлений деятельности). Разработка презентаций и аналитических "
                                                               "материалов для руководства Клуба")
    assert list_vacancy_object.list_object[-1].experience == "Требуемый опыт не указан"
    assert list_vacancy_object.list_object[-1].employment == "Полный день"


def test_create_list_class_object(list_dict_vacancy):
    """Тестирование метода создания списка объектов класса Vacancy"""
    list_vacancy_object = ListVacancyObject(list_dict_vacancy)
    list_vacancy_object.create_list_class_object()
    assert len(list_vacancy_object.list_object) == 3
    assert isinstance(list_vacancy_object.list_object[1], Vacancy) == True


def test_select_list_requirement(list_vacancy_class):
    """Тестирование метода выборки объектов класса Vacancy списка согласно заданному пользователем запросу"""
    list_vacancy_object = ListVacancyObject([])
    list_vacancy_object.list_object = list_vacancy_class
    list_vacancy_object.select_list_requirement("высшее образование")
    assert list_vacancy_object.list_select[0].name == "Специалист отдела маркетинга"
    assert list_vacancy_object.list_select[0].url == "https://hh.ru/vacancy/102987352"
    assert list_vacancy_object.list_select[0].salary_from == 50000
    assert list_vacancy_object.list_select[0].salary_to == 70000
    assert list_vacancy_object.list_select[0].requirement == ("Знание языков: Русский, Английский. Высшее образование."
                                                              "Уверенный пользователь ПК."
                                                              " Навыки работы с большими массивами данных."
                                                              " Аналитический склад ума.")
    assert list_vacancy_object.list_select[0].experience == "От 3 лет"
    assert list_vacancy_object.list_select[0].employment == "Полный день"


def test_sort_lists_salary(list_dict_vacancy):
    """Тестирование метода сортировки списка с объектами класса Vacancy"""
    list_vacancy_object = ListVacancyObject([])
    list_vacancy_object.list_select = list_dict_vacancy
    list_vacancy_object.sort_lists_salary()
    assert list_vacancy_object.list_sort[0]["name"] == "CRM-маркетолог"
    assert list_vacancy_object.list_sort[1]["name"] == "Редактор интернет-ресурса"
    assert list_vacancy_object.list_sort[2]["name"] == "Бренд-менеджер"


from src.Class_Vacancy import Vacancy


def test_vacancy_init(first_vacancy):
    """Тест конструктора класса"""
    assert first_vacancy.name == "Менеджер на переписки в чаты"
    assert first_vacancy.url == "https://hh.ru/vacancy/103008320"


def test_getter_salary_thirst(first_vacancy):
    """Тест геттера зарплаты"""
    assert first_vacancy.salary == [0, 80000]

def test_getter_salary_second(second_vacancy):
    """Тест геттера зарплаты"""
    assert second_vacancy.salary == [50000, 0]

def test_setter_salary(first_vacancy,salary_dict):
    """Тест сеттера зарплаты"""
    assert first_vacancy.salary == [0, 80000]
    first_vacancy.salary = salary_dict
    assert first_vacancy.salary == [50000, 150000]

def test_setter_salary_none(first_vacancy,salary_dict):
    """Тест сеттера зарплаты"""
    assert first_vacancy.salary == [0, 80000]
    first_vacancy.salary = None
    assert first_vacancy.salary == [0]


def test_getter_requirement_thirst(first_vacancy):
    """Тест геттера навыков"""
    assert first_vacancy.requirement == ("Наличие смартфона и стабильного интернета."
                                         "Желание зарабатывать и готовность обучаться."
                                         " Наличие ватсапа и телеграм на телефоне.")

def test_getter_requirement_second(second_vacancy):
    """Тест геттера навыков"""
    assert second_vacancy.requirement == "Требования не описаны"


def  test_setter_requirement(first_vacancy, snippet_dict):
    """Тест сеттера навыков"""
    assert first_vacancy.requirement == ("Наличие смартфона и стабильного интернета."
                                         "Желание зарабатывать и готовность обучаться."
                                         " Наличие ватсапа и телеграм на телефоне.")
    first_vacancy.requirement = snippet_dict
    assert first_vacancy.requirement == ("Будет плюсом: Навыки программирования на Java. Опыт разработки эмуляторов"
                                          "/заглушек на Java/Python. Опыт работы с Docker. Понимание оркестрации"
                                          " контейнеров.")


def  test_setter_requirement_none(first_vacancy, snippet_dict):
    """Тест сеттера навыков"""
    assert first_vacancy.requirement == ("Наличие смартфона и стабильного интернета."
                                         "Желание зарабатывать и готовность обучаться."
                                         " Наличие ватсапа и телеграм на телефоне.")
    first_vacancy.requirement = None
    assert first_vacancy.requirement == "Требования не описаны"


def test_getter_experience_thirst(first_vacancy):
    """Тест геттера опыта"""
    assert first_vacancy.experience == "Нет опыта"


def test_getter_experience_second(second_vacancy):
    """Тест геттера опыта"""
    assert second_vacancy.experience == "Требуемый опыт не указан"


def test_setter_experience(first_vacancy, experience_dict):
    """Тест сеттера опыта"""
    assert first_vacancy.experience == "Нет опыта"
    first_vacancy.experience = experience_dict
    assert first_vacancy.experience == "3 года"

def test_setter_experience_none(first_vacancy, experience_dict):
    """Тест сеттера опыта"""
    assert first_vacancy.experience == "Нет опыта"
    first_vacancy.experience = None
    assert first_vacancy.experience == "Требуемый опыт не указан"



def test_getter_employment_thirst(first_vacancy):
    """Тест геттера вида занятости"""
    assert first_vacancy.employment == "Полная занятость"


def test_getter_employment_second(second_vacancy):
    """Тест геттера вида занятости"""
    assert second_vacancy.employment == "Тип занятости не указан"


def test_setter_employment(first_vacancy, employment_dict):
    """Тест сеттера вида занятости"""
    assert first_vacancy.employment == "Полная занятость"
    first_vacancy.employment = employment_dict
    assert first_vacancy.employment == "Частичная занятость"


def test_setter_employment_none(first_vacancy, employment_dict):
    """Тест сеттера вида занятости"""
    assert first_vacancy.employment == "Полная занятость"
    first_vacancy.employment = None
    assert first_vacancy.employment == "Тип занятости не указан"



def test_vacancy_str_thirst(first_vacancy):
    """Тест строкового представления класса"""
    assert (str(first_vacancy) == "Вакансия: Менеджер на переписки в чаты Ссылка на вакансию: https://hh.ru/vacancy/103008320\n"
                                  "Зарплата в диапазоне от 0 до 80000\n"
                                  "Обязанности: Наличие смартфона и стабильного интернета."
                                 "Желание зарабатывать и готовность обучаться. Наличие ватсапа и телеграм на телефоне.\n"
                                  "Требуемый опыт: Нет опыта\n"
                                  "Тип занятости: Полная занятость\n")


def test_vacancy_str_second(first_vacancy):
    first_vacancy.salary = None
    assert (str(first_vacancy) == "Вакансия: Менеджер на переписки в чаты Ссылка на вакансию: https://hh.ru/vacancy/103008320\n"
                                  "Зарплата не указана\n"
                                  "Обязанности: Наличие смартфона и стабильного интернета."
                                 "Желание зарабатывать и готовность обучаться. Наличие ватсапа и телеграм на телефоне.\n"
                                  "Требуемый опыт: Нет опыта\n"
                                  "Тип занятости: Полная занятость\n")


def test_vacancy_lt(first_vacancy, second_vacancy):
    """Тест сравнения объектов класса по зарплате на меньше"""
    assert (first_vacancy.salary < second_vacancy.salary) == True


def test_vacancy_le(first_vacancy, second_vacancy):
    """Тест сравнения объектов класса по зарплате на меньше или равно"""
    assert (first_vacancy.salary <= second_vacancy.salary) == True


def test_vacancy_eq(first_vacancy, second_vacancy):
    """Тест сравнения объектов класса по зарплате на равно"""
    assert (first_vacancy.salary == second_vacancy.salary) == False


def test_vacancy_gt(first_vacancy, second_vacancy):
    """Тест сравнения объектов класса по зарплате на больше"""
    assert (first_vacancy.salary > second_vacancy.salary) == False


def test_vacancy_ge(first_vacancy, second_vacancy):
    """Тест сравнения объектов класса по зарплате на больше или равно"""
    assert (first_vacancy.salary >= second_vacancy.salary) == False


def test_new_vacancy(vacancy_dict_first):
    """Тест добавления нового объекта в список"""
    new_vacancy = Vacancy.new_vacancy("CRM-маркетолог", "https://hh.ru/vacancy/103943990")
    assert new_vacancy.name == "CRM-маркетолог"
    assert new_vacancy.url == "https://hh.ru/vacancy/103943990"


def test_sort_list_vacancy(list_vacancy_class):
    """Тестирование класс метода сортировки списка вакансий по зарплате"""
    sorted_list_vacancy = Vacancy.sort_list_vacancy(list_vacancy_class)
    assert sorted_list_vacancy[0].salary == [50000, 0]
    assert sorted_list_vacancy[1].salary == [0, 80000]


def test_crop_list_salary(list_vacancy_class):
    """Тестирование класс метода обрезки списка вакансий"""
    crop_vacancy_list = Vacancy.crop_list_salary(list_vacancy_class, "1")
    assert len(crop_vacancy_list) == 1


def test_select_list_requirement(list_vacancy_class):
    """Тестирование класс метода выборки объектов класса по свойству требований к вакансии
            из списка по запросу пользователя """
    select_requirement_list = Vacancy.select_list_requirement(list_vacancy_class, "Наличие смартфона")
    assert select_requirement_list[0].name == "Менеджер на переписки в чаты"
    assert select_requirement_list[0].requirement == ("Наличие смартфона и стабильного интернета."
                                                      "Желание зарабатывать и готовность обучаться. Наличие ватсапа и телеграм на телефоне.")

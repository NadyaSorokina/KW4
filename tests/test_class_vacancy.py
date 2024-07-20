from src.Class_Vacancy import Vacancy


def test_vacancy_init(first_vacancy):
    """Тест конструктора класса"""
    assert first_vacancy.name == "Менеджер на переписки в чаты"
    assert first_vacancy.url == "https://hh.ru/vacancy/103008320"
    assert first_vacancy.salary_from == 15000
    assert first_vacancy.salary_to == 30000
    assert first_vacancy.requirement == ("Наличие смартфона и стабильного интернета. "
                                         "Желание зарабатывать и готовность обучаться. Наличие ватсапа и телеграм на телефоне.")

    assert first_vacancy.experience == "Нет опыта"
    assert first_vacancy.employment == "Полная занятость"


def test_vacancy_str(first_vacancy):
    """Тест строкового представления класса"""
    assert (str(first_vacancy) == "Вакансия: Менеджер на переписки в чаты Ссылка на вакансию: https://hh.ru/vacancy/103008320\n"
                                  "Зарплата в диапазоне от 15000 до 30000\n"
                                  "Обязанности: Наличие смартфона и стабильного интернета. "
                                         "Желание зарабатывать и готовность обучаться. Наличие ватсапа и телеграм на телефоне.\n"
                                  "Требуемый опыт: Нет опыта\n"
                                  "Тип занятости: Полная занятость\n")


def test_vacancy_lt_first(first_vacancy, second_vacancy):
    """Тест сравнения объектов класса по зарплате на меньше"""
    assert (first_vacancy < second_vacancy) == True


def test_vacancy_lt_second(first_vacancy, third_vacancy):
    """Тест сравнения объектов класса по зарплате на меньше"""
    assert (first_vacancy < third_vacancy) == False


def test_vacancy_le_first(first_vacancy, second_vacancy):
    """Тест сравнения объектов класса по зарплате на меньше или равно"""
    assert (first_vacancy <= second_vacancy) == True


def test_vacancy_le_second(first_vacancy, third_vacancy):
    """Тест сравнения объектов класса по зарплате на меньше или равно"""
    assert (first_vacancy <= third_vacancy) == False


def test_vacancy_eq_first(first_vacancy, second_vacancy):
    """Тест сравнения объектов класса по зарплате на равно"""
    assert (first_vacancy == second_vacancy) == False


def test_vacancy_ne_second(first_vacancy, third_vacancy):
    """Тест сравнения объектов класса по зарплате на не равно"""
    assert (first_vacancy != third_vacancy) == True


def test_vacancy_gt_first(first_vacancy, second_vacancy):
    """Тест сравнения объектов класса по зарплате на больше"""
    assert (first_vacancy > second_vacancy) == False


def test_vacancy_gt_second(first_vacancy, third_vacancy):
    """Тест сравнения объектов класса по зарплате на больше"""
    assert (first_vacancy > third_vacancy) == True


def test_vacancy_ge_first(first_vacancy, second_vacancy):
    """Тест сравнения объектов класса по зарплате на больше или равно"""
    assert (first_vacancy > second_vacancy) == False


def test_vacancy_ge_second(first_vacancy, third_vacancy):
    """Тест сравнения объектов класса по зарплате на больше или равно"""
    assert (first_vacancy > third_vacancy) == True


def test_new_vacancy(vacancy_dict_first):
    """Тест добавления нового объекта в список"""
    new_vacancy = Vacancy.new_vacancy(vacancy_dict_first)
    assert new_vacancy.name == "CRM-маркетолог"
    assert new_vacancy.url == "https://hh.ru/vacancy/103943990"
    assert new_vacancy.salary_from == 120000
    assert new_vacancy.salary_to == 150000
    assert new_vacancy.requirement == ("Обязательный опыт работы с CDP (AltCraft - станет особенно большим плюсом). "
                                       "- Английский не ниже intermediate")
    assert new_vacancy.experience == "Требуемый опыт не указан"
    assert new_vacancy.employment == "Полный день"
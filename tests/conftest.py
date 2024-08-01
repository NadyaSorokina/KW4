import os

import pytest
from src.Class_Vacancy import Vacancy



@pytest.fixture
def first_vacancy():
    vacancy_first = Vacancy("Менеджер на переписки в чаты", "https://hh.ru/vacancy/103008320")
    vacancy_first.salary = {"from": None,
                            "to": 80000}
    vacancy_first.requirement = {"requirement": "Наличие смартфона и стабильного интернета."
                                 "Желание зарабатывать и готовность обучаться. Наличие ватсапа и телеграм на телефоне."}
    vacancy_first.experience = {"name": "Нет опыта"}
    vacancy_first.employment = {"name": "Полная занятость"}
    return vacancy_first


@pytest.fixture
def second_vacancy():
    vacancy_second = Vacancy("Специалист отдела маркетинга", "https://hh.ru/vacancy/102987352")
    vacancy_second.salary = {"from": 50000,
                            "to": None,}
    vacancy_second.requirement = {"requirement": None}
    vacancy_second.experience = {"name": None}
    vacancy_second.employment = {"name": None}
    return vacancy_second



@pytest.fixture
def  third_vacancy():
    vacancy_third = Vacancy("Специалист по стратегии и развитию", "https://hh.ru/vacancy/104170033")
    vacancy_third.salary = None
    vacancy_third.requirement = {"requirement": "Актуализация стратегий Клуба (коммерческой стратегии, спортивной стратегии,"
                                 "стратегий других отдельных направлений деятельности). Разработка презентаций и аналитических "
                                 "материалов для руководства Клуба"}
    vacancy_third.experience = None
    vacancy_third.employment = {"name": "Полный день"}

    return vacancy_third



@pytest.fixture
def vacancy_dict_first():
    return {"name": "CRM-маркетолог",
            "url": "https://hh.ru/vacancy/103943990",
            "salary_from": 120000,
            "salary_to": 150000,
            "requirement": ("Обязательный опыт работы с CDP (AltCraft - станет особенно большим плюсом). "
                             "- Английский не ниже intermediate"),

            "experience": "Требуемый опыт не указан",
            "employment": "Полный день"
            }

@pytest.fixture
def list_vacancy_class(first_vacancy,second_vacancy):
    return [first_vacancy, second_vacancy]


@pytest.fixture
def salary_dict():
    return {
            "from": 50000,
            "to": 150000,
    }

@pytest.fixture
def snippet_dict():
    return {
            "requirement": "Будет плюсом: Навыки программирования на Java. Опыт разработки эмуляторов/заглушек на Java/Python. Опыт работы с Docker. Понимание оркестрации контейнеров.",
            "responsibility": "Мониторинг JVM, ключевые метрики производительности."
        }

@pytest.fixture
def experience_dict():
    return {"id": "noExperience",
            "name": "3 года"}


@pytest.fixture
def employment_dict():
    return {"id": "full",
            "name": "Частичная занятость"}

#Пути к тестовому JSON файлу
ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(ROOT_PATH, 'tests')
VACANCY_PATH = os.path.join(DATA_PATH, 'json_test.json')
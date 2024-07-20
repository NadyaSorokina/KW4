import pytest
from src.Class_Vacancy import Vacancy



@pytest.fixture
def first_vacancy():
    return Vacancy("Менеджер на переписки в чаты", "https://hh.ru/vacancy/103008320", 15000,
                   30000,
                   "Наличие смартфона и стабильного интернета. "
                   "Желание зарабатывать и готовность обучаться. Наличие ватсапа и телеграм на телефоне.",
                   "Нет опыта", "Полная занятость")


@pytest.fixture
def second_vacancy():
    return Vacancy("Специалист отдела маркетинга", "https://hh.ru/vacancy/102987352", 50000,
                   70000,
                   "Знание языков: Русский, Английский. Высшее образование."
                   "Уверенный пользователь ПК. Навыки работы с большими массивами данных. Аналитический склад ума.",
                   "От 3 лет", "Полный день")



@pytest.fixture
def  third_vacancy():
    return Vacancy("Специалист по стратегии и развитию", "https://hh.ru/vacancy/104170033", 0,
                   0,
                   "Актуализация стратегий Клуба (коммерческой стратегии, спортивной стратегии, "
                   "стратегий других отдельных направлений деятельности). Разработка презентаций и аналитических "
                   "материалов для руководства Клуба",
                   "Требуемый опыт не указан", "Полный день")



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
def list_dict_vacancy():
    return [
        {
        "name": "CRM-маркетолог",
        "url": "https://hh.ru/vacancy/103943990",
        "salary_from": 120000,
        "salary_to": 150000,
        "requirement": ("Обязательный опыт работы с CDP (AltCraft - станет особенно большим плюсом). "
                        "- Английский не ниже intermediate"),

        "experience": "Требуемый опыт не указан",
        "employment": "Полный день"
        },
        {
        "name": "Бренд-менеджер",
        "url": "https://hh.ru/vacancy/104160480",
        "salary_from": 0,
        "salary_to": 0,
        "requirement": "Знание принципов SMM и опыт работы с аккаунтами.",
        "experience": "От года",
        "employment": "Полный день"

        },
        {
        "name": "Редактор интернет-ресурса",
        "url": "https://hh.ru/vacancy/103138060",
        "salary_from": 700,
        "salary_to": 1400,
        "requirement": "Опыт работы в аналогичной должности будет преимуществом. Аналитический склад ума.",
        "experience": "Требуемый опыт не указан",
        "employment": "Полный день"
        }
    ]

@pytest.fixture
def list_vacancy_class(first_vacancy,second_vacancy):
    return [first_vacancy, second_vacancy]


@pytest.fixture
def list_not_validate():
    return[ {
            "name": "Начинающий специалист (менеджер на переписки в чаты)",
            "salary": {
                "from": 15000,
                "to": None,
            },
            "alternate_url": "https://hh.ru/vacancy/103008320",
            "snippet": {
                "requirement": "Наличие смартфона и стабильного интернета. Желание зарабатывать и готовность обучаться. Наличие ватсапа и телеграм на телефоне.",
                "responsibility": 0
            },
            "accept_incomplete_resumes": True,
            "experience": {
                "id": "noExperience",
                "name": None
            },
            "employment": None
    }]


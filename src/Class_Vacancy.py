class Vacancy:
    """Класс для создания и обратки вакансий"""
    name: str
    link: str
    salary_from: int
    salary_to: int
    requirement: str
    experience: str
    employment: str


    def __init__(self, name: str, url: str, salary_from: int, salary_to: int, requirement: str, experience: str, employment: str):
         """Конструктор класса Vacancy"""
         self.name = name
         self.url = url
         self.salary_from = salary_from
         self.salary_to = salary_to
         self.requirement = requirement
         self.experience = experience
         self.employment = employment


    def __str__(self):
        """Строковое представление класса Vacancy для пользователя"""
        return (f"Вакансия: {self.name} Ссылка на вакансию: {self.url}\n"
                f"Зарплата в диапазоне от {self.salary_from} до {self.salary_to}\n"
                f"Обязанности: {self.requirement}\n"
                f"Требуемый опыт: {self.experience}\n"
                f"Тип занятости: {self.employment}\n")


    def __lt__(self, other: 'Vacancy'):
        """Метод "меньше" сравнения для зарплат вакансий"""
        if not isinstance(other, Vacancy):
            raise TypeError(f"Некорректный тип для сравнения с классом Vacancy: {other.__class__.__name__}")
        return self.salary_to < other.salary_to and self.salary_from < other.salary_from


    def __le__(self, other: 'Vacancy'):
        """Метод "меньше или равно" сравнения для зарплат вакансий"""
        if not isinstance(other, Vacancy):
            raise TypeError(f"Некорректный тип для сравнения с классом Vacancy: {other.__class__.__name__}")
        return self.salary_to <= other.salary_to and self.salary_from <= other.salary_from


    def __eq__(self, other: 'Vacancy'):
        """Метод "равно" сравнения для зарплат вакансий"""
        if not isinstance(other, Vacancy):
            raise TypeError(f"Некорректный тип для сравнения с классом Vacancy: {other.__class__.__name__}")
        return self.salary_to == other.salary_to and self.salary_from == other.salary_from


    def __ne__(self, other: 'Vacancy'):
        """Метод "не равно" сравнения для зарплат вакансий"""
        if not isinstance(other, Vacancy):
            raise TypeError(f"Некорректный тип для сравнения с классом Vacancy: {other.__class__.__name__}")
        return self.salary_to != other.salary_to and self.salary_from != other.salary_from


    def __gt__(self, other: 'Vacancy'):
        """Метод "больше" сравнения для зарплат вакансий"""
        if not isinstance(other, Vacancy):
            raise TypeError(f"Некорректный тип для сравнения с классом Vacancy: {other.__class__.__name__}")
        return self.salary_to > other.salary_to and self.salary_from > other.salary_from


    def __ge__(self, other: 'Vacancy'):
        """Метод "больше или равно" сравнения для зарплат вакансий"""
        if not isinstance(other, Vacancy):
            raise TypeError(f"Некорректный тип для сравнения с классом Vacancy: {other.__class__.__name__}")
        return self.salary_to >= other.salary_to and self.salary_from >= other.salary_from


    @classmethod
    def new_vacancy(cls, vacancy):
        """Метод по созданию нового экземпляра класса"""
        return cls(**vacancy)


    def __del__(self):
        """ Деструктор объекта класса Vacancy"""
        return "Объект удален"


class Vacancy:
    """Класс для создания и обратки вакансий"""
    name: str
    url: str

    def __init__(self, name: str, url: str):
         """Конструктор класса Vacancy"""
         self.name = name
         self.url = url
         self.__salary = []
         self.__requirement = ''
         self.__experience = ''
         self.__employment =  ''


    def __str__(self):
        """Строковое представление класса Vacancy для пользователя"""
        if len(self.salary) < 2 and self.salary[0] == 0:
            return (f"Вакансия: {self.name} Ссылка на вакансию: {self.url}\n"
                    f"Зарплата не указана\n"
                    f"Обязанности: {self.__requirement}\n"
                    f"Требуемый опыт: {self.__experience}\n"
                    f"Тип занятости: {self.__employment}\n")

        else:
            return (f"Вакансия: {self.name} Ссылка на вакансию: {self.url}\n"
                    f"Зарплата в диапазоне от {self.__salary[0]} до {self.__salary[1]}\n"
                    f"Обязанности: {self.__requirement}\n"
                    f"Требуемый опыт: {self.__experience}\n"
                    f"Тип занятости: {self.__employment}\n")


    @property
    def salary(self):
        """Вывод данных по зарплате"""
        return self.__salary


    @salary.setter
    def salary(self, salary_dict):
        """Установка данных по зарплате"""
        self.__salary = []
        if salary_dict is None:
            self.__salary.append(0)
        else:
            for key, value in salary_dict.items():
                    if salary_dict[key] is None:
                        self.__salary.append(0)
                    else:
                        self.__salary.append(salary_dict[key])


    @property
    def requirement(self):
        """Вывод данных по навыкам"""
        return self.__requirement


    @requirement.setter
    def requirement(self, snippet_dict):
        """Установка данных по навыкам"""
        if snippet_dict is None:
            self.__requirement = "Требования не описаны"
        else:
            for key, value in snippet_dict.items():
                if key == "requirement":
                        if snippet_dict[key] is None:
                            self.__requirement = "Требования не описаны"
                        else:
                            self.__requirement = (snippet_dict[key].replace("<highlighttext>", "").
                                                  replace("</highlighttext>", ""))
                else:
                    continue



    @property
    def experience(self):
        """Вывод данных по опыту"""
        return self.__experience


    @experience.setter
    def experience(self, experience_dict):
        """Установка данных по опыту"""
        if experience_dict is None:
            self.__experience = "Требуемый опыт не указан"
        else:
            for key, value in experience_dict.items():
                    if key == "name":
                        if experience_dict[key] is None:
                            self.__experience = "Требуемый опыт не указан"
                        else:
                            self.__experience = (experience_dict[key].replace("<highlighttext>", "").
                                                  replace("</highlighttext>", ""))
                    else:
                        continue


    @property
    def employment(self):
        """Вывод данных по занятости"""
        return self.__employment


    @employment.setter
    def employment(self, employment_dict):
        """Установка данных по занятости"""
        if employment_dict is None:
            self.__employment = "Тип занятости не указан"
        else:
            for key, value in employment_dict.items():
                if key == "name":
                    if employment_dict[key] is None:
                        self.__employment = "Тип занятости не указан"
                    else:
                            self.__employment = (employment_dict[key])
                else:
                        continue


    def __lt__(self, other: 'Vacancy'):
        """Метод "меньше" сравнения для зарплат вакансий"""
        if not isinstance(other, Vacancy):
            raise TypeError(f"Некорректный тип для сравнения с классом Vacancy: {other.__class__.__name__}")
        return self.__salary[0] < other.__salary[0] and self.__salary[1] < other.__salary[1]


    def __le__(self, other: 'Vacancy'):
        """Метод "меньше или равно" сравнения для зарплат вакансий"""
        if not isinstance(other, Vacancy):
            raise TypeError(f"Некорректный тип для сравнения с классом Vacancy: {other.__class__.__name__}")
        return self.__salary[0] <= other.__salary[0]


    def __eq__(self, other: 'Vacancy'):
        """Метод "равно" сравнения для зарплат вакансий"""
        if not isinstance(other, Vacancy):
            raise TypeError(f"Некорректный тип для сравнения с классом Vacancy: {other.__class__.__name__}")
        return self.__salary[0] == other.__salary[0]


    def __ne__(self, other: 'Vacancy'):
        """Метод "не равно" сравнения для зарплат вакансий"""
        if not isinstance(other, Vacancy):
            raise TypeError(f"Некорректный тип для сравнения с классом Vacancy: {other.__class__.__name__}")
        return self.__salary[0] != other.__salary[0]

    def __gt__(self, other: 'Vacancy'):
        """Метод "больше" сравнения для зарплат вакансий"""
        if not isinstance(other, Vacancy):
            raise TypeError(f"Некорректный тип для сравнения с классом Vacancy: {other.__class__.__name__}")
        return self.__salary[0] > other.__salary[0]


    def __ge__(self, other: 'Vacancy'):
        """Метод "больше или равно" сравнения для зарплат вакансий"""
        if not isinstance(other, Vacancy):
            raise TypeError(f"Некорректный тип для сравнения с классом Vacancy: {other.__class__.__name__}")
        return self.__salary[0] >= other.__salary[0]


    @classmethod
    def new_vacancy(cls, name: str, url: str):
        """Метод по созданию нового экземпляра класса"""
        return cls(name, url)


    @classmethod
    def sort_list_vacancy(cls, list_vacancy: list):
        """Метод сортировки списка с вакансиями"""
        sorted_list_vacancy = sorted(list_vacancy, key=lambda  vacancy: vacancy.__salary[0],
                                   reverse=True)

        return sorted_list_vacancy


    @classmethod
    def crop_list_salary(cls, list_vacancy: list, vacancy_count: str ):
        """Метод обрезки списка по длине, инициализированной
            в объекте класса"""
        vacancy_crop_list = list_vacancy.copy()
        return vacancy_crop_list[:int(vacancy_count)]


    @classmethod
    def select_list_requirement(cls, list_vacancy: list, user_request: str):
        """Метод выборки объектов класса по свойству требований к вакансии
            из списка по запросу пользователя"""
        list_user_request = user_request.split()
        select_list_vacancy = []
        for element in list_vacancy:
            count_entry = 0
            for request_element in list_user_request:
                if request_element.lower() in element.__requirement.lower():
                    count_entry += 1
            if count_entry > 0:
                select_list_vacancy.append(element)
            else:
                continue
        return select_list_vacancy

    def __del__(self):
        """ Деструктор объекта класса Vacancy"""
        return "Объект удален"

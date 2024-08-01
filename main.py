from src.Class_APIConnection import HHIntegration
from src.Class_ListModification import ListModification, JsonToList
from src.Class_LoadRequests import JsonLoadRequests
from src.Class_Parser import HH
from src.Class_Vacancy import Vacancy
from src.class_ListClassObject import ListVacancyObject
from src.config import VACANCY_PATH, RESULT_VACANCY_PATH



def main():

    keyword = input(f"Начнем поиск по вакансия HH.ru. Укажите название вакансии для поиска: \n").lower()

    #Загрузка данных с ресурса
    integration_hh = HHIntegration()
    print(integration_hh.response_check())

    # Загрузка данных с ресурса
    hh_parser = HH()
    hh_parser.load_vacancies(keyword)

    # Загрузка в файл Json
    json_hh_parser = JsonLoadRequests(hh_parser.vacancies)
    json_hh_parser.path = VACANCY_PATH
    json_hh_parser.write_requests()

    # Загрузка данных из файла Json в список
    vacancy_list = JsonToList(VACANCY_PATH).modification_list()

    if len(vacancy_list) == 0:
        print("По Вашему запросу ничего не найдено. Попробуйте заново.")
        return
    else:

        # Формирование и вывод списка объектов класса Vacancy
        list_class_vacancy = ListVacancyObject()
        list_class_vacancy.create_list_class_object(vacancy_list)

        sorted_list_vacancy = Vacancy.sort_list_vacancy(list_class_vacancy.list_object)

        vacancy_count = input("Мы загрузили для Вас список топ-вакансий по зарплате.\n"
                              f"Всего загружено {len(list_class_vacancy.list_object)} вакансий.\n"
                             "Введите количество вакансий, которые хотите просмотреть:\n")

        while not vacancy_count.isdigit():
                vacancy_count = input("Введите количество цифрой:\n")
        else:
            print("Вакансии по Вашему запросу")

            crop_vacancy_list = Vacancy.crop_list_salary(sorted_list_vacancy, vacancy_count)
            for vacancy in crop_vacancy_list:
                print(f"{vacancy}\n")

        # Формирование и вывод списка объектов класса Vacancy по ключевому слову в требованиях
        user_request = input("Введите ключевые слова для поиска по требованиям.\n"
                                        "Несколько ключевых слов вводите через пробел:\n")
        print("Вакансии по Вашему запросу:")

        select_requirement_list = Vacancy.select_list_requirement(crop_vacancy_list, user_request)
        for select_vacancy in select_requirement_list:
            print(f"{select_vacancy}\n")

        # Очищение JSON файла
        #json_hh_parser.clear_json()


if __name__ == '__main__':
    main()

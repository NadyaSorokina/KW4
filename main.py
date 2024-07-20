from src.Class_APIConnection import HHIntegration
from src.Class_ListModification import ListModification, ListToValidateList, SortList, CropList, JsonToList
from src.Class_LoadRequests import JsonLoadRequests
from src.Class_Parser import HH
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
    json_hh_parser = JsonLoadRequests(hh_parser.vacancies, VACANCY_PATH)
    json_hh_parser.write_requests()
   # vacancy_list = json_hh_parser.json_to_list()
    # Загрузка данных из файла Json в список
    vacancy_list = JsonToList(VACANCY_PATH).modification_list()

    # Преобразование загруженного списка в список с валидированными данными
    vacancy_list_to_list = ListToValidateList(vacancy_list)

    #Сортировка валидированного списка по зп
    vacancy_sort_list = SortList(vacancy_list_to_list.modification_list())

    #Формирование списка заданной пользователем длины
    vacancy_count = input("Мы загрузили для Вас список топ-вакансий по зарплате.\n"
                          "Введите количество вакансий, которые хотите просмотреть:\n")
    while not vacancy_count.isdigit():
        vacancy_count = input("Введите количество цифрой:\n")
    else:
        print("Вакансии по Вашему запросу")
        vacancy_crop_list = CropList(vacancy_sort_list.modification_list(), vacancy_count).modification_list()
        #print(vacancy_crop_list)

        #Формирование и вывод списка объектов класса Vacancy
        list_class_vacancy = ListVacancyObject(vacancy_crop_list)
        list_class_vacancy.create_list_class_object()
        for vacancy in list_class_vacancy.list_object:
            print(f"{vacancy}\n")

        #Формирование и вывод списка объектов класса Vacancy по ключевому слову в требованиях
        user_request = input("Введите ключевые слова для поиска по требованиям.\n"
                            "Несколько ключевых слов вводите через пробел:\n")
        print("Вакансии по Вашему запросу:")
        list_class_vacancy.select_list_requirement(user_request)
        for element in list_class_vacancy.list_select:
            print(element)

    #Очищение JSON файла
    json_hh_parser.clear_json()


if __name__ == '__main__':
    main()
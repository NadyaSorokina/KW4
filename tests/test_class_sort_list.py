from src.Class_ListModification import SortList


def test_sort_list(list_dict_vacancy):
    """Тестирование метода сортировки списка"""
    vacancy_list = SortList(list_dict_vacancy)
    vacancy_sort_list = vacancy_list.modification_list()
    assert vacancy_sort_list[0]["salary_from"] == 120000
    assert vacancy_sort_list[0]["salary_to"] == 150000
    assert vacancy_sort_list[1]["salary_from"] == 700
    assert vacancy_sort_list[1]["salary_to"] == 1400
    assert vacancy_sort_list[2]["salary_from"] == 0
    assert vacancy_sort_list[2]["salary_to"] == 0
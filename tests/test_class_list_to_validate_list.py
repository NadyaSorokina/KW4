from src.Class_ListModification import ListToValidateList


def test_modification_list(list_not_validate):
    """Тестирование метода валидации данных списка"""
    list_vacancy = ListToValidateList(list_not_validate)
    list_dict_validate = list_vacancy.modification_list()
    assert list_dict_validate[0]["salary_to"] == 0
    assert list_dict_validate[0]["employment"] == "Тип занятости не указан"
    assert list_dict_validate[0]["experience"] == "Требуемый опыт не указан"

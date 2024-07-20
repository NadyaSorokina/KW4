from src.Class_ListModification import CropList


def test_crop_list(list_dict_vacancy):
    """Тестирование метода обрезки списка"""
    vacancy_list = CropList(list_dict_vacancy, "2")
    vacancy_crop_list = vacancy_list.modification_list()
    assert len(vacancy_crop_list) == 2

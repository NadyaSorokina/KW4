import os

# строим пути для файлов
ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(ROOT_PATH, 'data')
VACANCY_PATH = os.path.join(DATA_PATH, 'vacancy_parser.json')
RESULT_VACANCY_PATH = os.path.join(DATA_PATH, 'vacancy')
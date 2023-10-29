""" Модуль констант для проекта pep_parse."""


from pathlib import Path

# Формат даты для имени файла
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

EXPECTED_STATUSES_LIST = (
    'Active',
    'Accepted',
    'Deferred',
    'Draft',
    'Final',
    'Provisional',
    'Rejected',
    'Superseded',
    'Withdrawn',
)

RESULTS_DIR_NAME = 'results'
# Каталог для сохранение результатов работы пайплайна PepParsePipeline
BASE_DIR = Path(__file__).absolute().parent.parent / RESULTS_DIR_NAME
# Заголовки для таблицы результатов работы пайплайна PepParsePipeline
STATUS_SUMMURY_HEADER = (
    'Статус',
    'Количество',
)

UNKNOWN_STATUS_NAME = 'Unknown'

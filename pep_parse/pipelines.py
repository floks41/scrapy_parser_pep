""" Модуль пайплайнов Scrapy для проекта pep_parse."""


import csv
import datetime as dt

from pep_parse.constants import (
    BASE_DIR,
    DATETIME_FORMAT,
    EXPECTED_STATUSES_LIST,
    STATUS_SUMMURY_HEADER,
    UNKNOWN_STATUS_NAME,
)


class PepParsePipeline:
    """Класс пайплайн для паука PepSpider."""

    def open_spider(self, spider):
        """Создает частотный словарь статусов документов pep
        при запуске паука."""
        self.freq_dict = {}

    def process_item(self, item, spider):
        """При обработке item c информацие о документе pep,
        заполняет частотный словарь."""

        current_status = item.get('status')
        if current_status not in EXPECTED_STATUSES_LIST:
            current_status = UNKNOWN_STATUS_NAME

        if self.freq_dict.get(current_status) is not None:
            self.freq_dict[current_status] += 1
        else:
            self.freq_dict[current_status] = 1

        return item

    def close_spider(self, spider):
        """По окончании работы паука сохраныет результаты подсчета в файл."""

        # Подсчет и формирование таблицы с результатами подсчета.
        total_peps_number = 0
        results = [
            STATUS_SUMMURY_HEADER,
        ]
        for key, value in self.freq_dict.items():
            results.append((key, value))
            total_peps_number += value
        results.append(('Total', total_peps_number))

        # Формируем имя файла с указанием внем даты и времени.
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'

        # Запись результатов в файл.
        try:
            BASE_DIR.mkdir(exist_ok=True)
            file_path = BASE_DIR / file_name
            with open(file_path, 'w', encoding='utf-8') as file:
                writer = csv.writer(
                    file, dialect='unix', quoting=csv.QUOTE_MINIMAL
                )
                writer.writerows(results)
        except Exception as exception:
            spider.logger.error(
                f'Не удалось сохранить файл {str(file_path)}.'
                f'Ошибка: {str(exception)}',
                stack_info=True,
            )

# Проект парсинга документов PEP — Python Enhancement Proposal (предложений по улучшению Python) PEP_parse на базе фреймворка Scrapy

### Разработчик (исполнитель):

👨🏼‍💻Олег Чужмаров: https://github.com/floks41

### Технологии
- Python 3.9
- Scrapy 2.5.1

1. Установка
- Скопировать каталог с проектом (scrapy_parser_pep) в место установки.
- В каталоге проекта (scrapy_parser_pep) установить и запустить виртуальное окружение:
```
/scrapy_parser_pep $ python3 -m venv venv
```
```
/scrapy_parser_pep $ source venv/bin/activate
```
- Обновить менеджер пакетов PIP и установить зависимости:
```
(venv) .../scrapy_parser_pep $ python3 -m pip install --upgrade pip
```
```
(venv) .../scrapy_parser_pep $ pip install -r requirements.txt
```

2. Использование (запуск из командной строки). В каталоге проекта (scrapy_parser_pep).
```
(venv) .../scrapy_parser_pep $ scrapy crawl pep
```
3. Функции.
- результаты работы парсера сохраняются в каталоге 'results' внутри каталога проекта (scrapy_parser_pep/results/).
- в файле pep_ДатаВремя.csv сохраняется список документов в PEP с указанием их номеров, наименований и текущего статуса.
- в файле status_summary_ДатаВремя.csv сохраняется сводка по количеству документов в предусмотренных статусах.

4. Код проекта проверен flake8 после линтинга isort и black:

```
isort pep_parse/.
```
```
isort pep_parse/spiders/.
```
```
black pep_parse/. --line-length 79 --skip-string-normalization
```
```
black pep_parse/spiders/. --line-length 79 --skip-string-normalization
```
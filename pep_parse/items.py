""" Модуль items фреймворка Scrapy для проекта pep_parse."""


import scrapy


class PepParseItem(scrapy.Item):
    """Класс item для паука PepSpider."""
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()

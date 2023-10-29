""" Модуль настроек Scrapy для проекта pep_parse."""


from pep_parse.constants import RESULTS_DIR_NAME

BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [
    NEWSPIDER_MODULE,
]

ROBOTSTXT_OBEY = True

FEED_EXPORT_ENCODING = "utf-8"

FEEDS = {
    (RESULTS_DIR_NAME + '/pep_%(time)s.csv'): {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

LOG_LEVEL = 'INFO'

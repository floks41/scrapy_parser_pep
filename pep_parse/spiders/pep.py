""" Модуль паука pep для проекта pep_parse."""


import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Паук для парсинга информации о статусах документов PEP."""

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Парсит таблицу с документами PEP, вызывает функцию
        pep_parse парсинга информации со страницы каждого документа."""
        table_rows = response.xpath(
            '//*[@id="numerical-index"]//table//tbody//tr'
        )
        for row in table_rows:
            pep_number = row.css('a::text').get()
            pep_name = row.css('td:nth-child(3) > a::text').get()
            pep_link = row.css('td:nth-child(3) > a::attr(href)').get()
            data = {'number': pep_number, 'name': pep_name, 'status': ''}
            item = PepParseItem(data)

            yield response.follow(
                pep_link, callback=self.parse_pep, cb_kwargs={'item': item}
            )

    def parse_pep(self, response, item):
        """Парсит информацию о статусе документа PEP
        со страницы конкретного документа."""

        pep_status = response.css(
            '#pep-content > dl > dt:contains("Status") + dd > abbr::text'
        ).get()
        item['status'] = pep_status
        yield item

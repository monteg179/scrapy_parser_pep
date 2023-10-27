import re

import scrapy
from scrapy.http.response.text import TextResponse as Response

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response: Response):
        links = response.xpath(
            '//*[@id="numerical-index"]//a[starts-with(@href, "pep-")]/@href'
        ).getall()
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response: Response):
        section = response.css('#pep-content')
        header = section.xpath('./h1//text()').getall()
        match = re.search(
            pattern=r'PEP (?P<number>\d+) (?:–|-) (?P<name>.+)',
            string=' '.join(header).strip()
        )
        if match:
            number, name = match.groups()
        else:
            number = None
            name = None
        status = section.xpath(
            '//dt[contains(., "Status")]/following-sibling::dd/abbr/text()'
        ).get()
        yield PepParseItem({'number': number, 'name': name, 'status': status})

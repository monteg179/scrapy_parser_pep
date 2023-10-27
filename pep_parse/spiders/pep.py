import scrapy
from scrapy.http.response.text import TextResponse as Response

from pep_parse.items import PepParseItem
from pep_parse.settings import (
    PEP_SPIDER_DOMAIN,
    PEP_SPIDER_NAME,
    PEP_SPIDER_URL,
)


class PepSpider(scrapy.Spider):

    name = PEP_SPIDER_NAME
    allowed_domains = [PEP_SPIDER_DOMAIN]
    start_urls = [PEP_SPIDER_URL]

    def parse(self, response: Response):
        links = response.xpath(
            '//*[@id="numerical-index"]//a[starts-with(@href, "pep-")]/@href'
        ).getall()
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response: Response):
        section = response.css('#pep-content')
        header = section.xpath('./h1//text()').getall()
        pep_number, name = ' '.join(header).strip().split(' – ', 1)
        status = section.xpath(
            '//dt[contains(., "Status")]/following-sibling::dd/abbr/text()'
        ).get()
        yield PepParseItem(
            {'number': pep_number.split()[1], 'name': name, 'status': status}
        )

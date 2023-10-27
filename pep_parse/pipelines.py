import datetime as dt
import csv

from scrapy.exceptions import DropItem

from pep_parse.items import PepParseItem
from pep_parse.settings import (
    BASE_DIR,
    DATETIME_FORMAT,
    PEP_STATUSES,
    RESULTS_FOLDER,
    SUMMARY_FILE_NAME,
    SUMMARY_HEADER,
)


class PepParsePipeline:

    def open_spider(self, spider) -> None:
        self.__summary = {}
        for status in PEP_STATUSES:
            self.__summary[status] = 0

    def close_spider(self, spider) -> None:
        self.__summary['Total'] = sum(self.__summary.values())
        self.save_summary()

    def process_item(self, item: PepParseItem, spider) -> PepParseItem:
        if any(item.fields.values()):
            raise DropItem('неудачный парсинг')
        status = item['status']
        if status not in PEP_STATUSES:
            raise DropItem('непонятный статус')
        self.__summary[status] += 1
        return item

    def save_summary(self) -> None:
        now = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = SUMMARY_FILE_NAME.format(now)
        path = BASE_DIR / RESULTS_FOLDER / file_name
        with open(path, 'w', encoding='utf-8') as file:
            writer = csv.writer(file, dialect='unix')
            writer.writerows((SUMMARY_HEADER, *self.__summary.items()))

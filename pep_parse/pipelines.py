import datetime as dt
import csv

from scrapy.exceptions import DropItem

from pep_parse.items import PepParseItem
from pep_parse.settings import (
    BASE_DIR,
    RESULTS_FOLDER,
)


class PepParsePipeline:

    STATUSES = (
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

    SUMMARY_FILE_NAME = 'status_summary_{}.csv'
    DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
    SUMMARY_HEADER = ('Статус', 'Количество')

    def open_spider(self, spider) -> None:
        self.__summary = {}
        for status in type(self).STATUSES:
            self.__summary[status] = 0

    def close_spider(self, spider) -> None:
        self.__summary['Total'] = sum(self.__summary.values())
        self.save_summary()

    def process_item(
            self, item: PepParseItem, spider) -> PepParseItem:
        number = item['number']
        name = item['name']
        status = item['status']
        if (number is None) or (name is None) or (status is None):
            raise DropItem('неудачный парсинг')
        if status not in type(self).STATUSES:
            raise DropItem('непонятный статус')
        self.__summary[status] += 1
        return item

    def save_summary(self) -> None:
        now = dt.datetime.now().strftime(type(self).DATETIME_FORMAT)
        file_name = type(self).SUMMARY_FILE_NAME.format(now)
        path = BASE_DIR / RESULTS_FOLDER / file_name
        with open(path, 'w', encoding='utf-8') as file:
            writer = csv.writer(file, dialect='unix')
            writer.writerows(
                (type(self).SUMMARY_HEADER, *self.__summary.items())
            )

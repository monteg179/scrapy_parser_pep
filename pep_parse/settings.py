from pathlib import Path

BOT_NAME = 'pep_parse'
SPIDER_MODULES = ['pep_parse.spiders']
ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent
RESULTS_FOLDER = 'results'

PEP_SPIDER_NAME = 'pep'
PEP_SPIDER_DOMAIN = 'peps.python.org'
PEP_SPIDER_URL = 'https://peps.python.org/'

PEP_STATUSES = (
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

LOG_LEVEL = 'INFO'

FEEDS = {
    f'{RESULTS_FOLDER}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

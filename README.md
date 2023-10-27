# АСИНХРОННЫЙ ПАРСЕР PEP

## ОПИСАНИЕ ПРОЕКТА
Проект - консольное приложение Python, которое выполняет парсинг документов PEP и сохраняет результат в CSV-файлах.

## ОСОБЕННОСТИ ПРОЕКТА
Использование фреймворка Scrapy

## ЗАПУСК ПРОЕКТА
1. клонировать проект
```
git clone git@github.com:monteg179/scrapy_parser_pep.git
```
2. создать, активировать и настроить виртуальное окружение
```
cd scrapy_parser_pep
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
3. запустить приложение
```
scrapy crawl pep
```

## ТЕХНОЛОГИИ
- Python 3.9
- Scrapy
- CSV

## АВТОРЫ
* Сергей Кузнецов - monteg179@yandex.ru



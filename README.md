# api_yatube

## Описание
Всё та же социальная сеть для публикаций личных дневников, только написанная **при помощи API.**

На сайте этой социальной сети можно создать свою страницу. Если на нее зайти, то можно посмотреть все записи автора.
Пользователи смогут заходить на чужие страницы, подписываться на авторов и комментировать их записи.
Автор может выбрать имя и уникальный адрес для своей страницы.

## Технологии в проекте
Python 3.7

Django 2.2.19

AuthToken

SQLite3

## Инструкции по запуску
### Клонировать репозиторий
```
git clone https://github.com/GandraNNA/api_yatube.git
```

### Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/bin/activate
```
В PyCharm активировать виртуальное окружение в терминале можно так:
```
.\venv\Scripts\activate.ps1
```
### Установить зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
### Выполнить миграции:
```
python manage.py migrate
```

### Запустить проект:
В папке с файлом manage.py выполните команду:
```
python manage.py runserver
```

#### _**Автор: Гандрабура Анна**_

# Обрезка ссылок с помощью Битли

Скрипт сокращает ссылки и считает количество кликов по короткой ссылке.

### Как установить

Чтобы получить токен нужно авторизироваться на Bitly. После того как получось достать токен нужно создать файл .env и положить данный токен в виде:
```
BITLY_APIKEY=Ваш токен
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить скрипт

Для запуска скрипта пишите команду:
```
python main.py ВАША_ССЫЛКА
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
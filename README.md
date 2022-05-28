# tennis-finder

[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

## Описание

Система, которая помогает находить партнеров для игры в теннис по рейтингу. Рейтинг считается исходя из уровня игры пользователя и побед/поражений каждого игрока. Каждый сыгранный матч можно заносить в систему и на основе новых данных рейтинг пересчитывается. 

## Инструменты

* Flask
* Jinja2
* sqlalchemy
* Babel
* flake8

## Локализация

Система поддерживает два языка: русский и английский, переключать язык можно нажав на флаг в правом верхнем углу страницы

``` shell
pybabel compile -f -d tennis_finder/translations
```

## Документация
``` shell
cd docs
sphinx-apidoc -o . ..
make clean html
```

Сгенерированная страница с документацией будет лежать в _build/html/index.html

## Макет интерфейса

![image](https://user-images.githubusercontent.com/36276118/170238451-bad94936-a568-457c-9f3f-e4e2d5bd9f07.png)
![image](https://user-images.githubusercontent.com/36276118/170238486-eb87dc80-d014-453c-bf24-e0409993b1f0.png)


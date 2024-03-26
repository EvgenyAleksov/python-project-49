### Hexlet tests and linter status:
[![Actions Status](https://github.com/EvgenyAleksov/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/EvgenyAleksov/python-project-49/actions)


[![Maintainability](https://api.codeclimate.com/v1/badges/da1d813750c6909348f7/maintainability)](https://codeclimate.com/github/EvgenyAleksov/python-project-49/maintainability)


# Проект Игры разума
**«Игры разума»** — набор из пяти консольных игр.
Каждая игра задает вопросы, на которые нужно дать правильные ответы.
Игра считается пройденной после трёх правильных ответов.
Неправильный ответ на любом шаге завершает игру, после чего предлагается пройти её заново.


**Игры:**

* [Проверка на чётность.](https://github.com/EvgenyAleksov/python-project-49/edit/main/README.md#%D0%B8%D0%B3%D1%80%D0%B0-%D0%BA%D0%B0%D0%BB%D1%8C%D0%BA%D1%83%D0%BB%D1%8F%D1%82%D0%BE%D1%80:~:text=%C2%AB%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0%20%D0%BD%D0%B0%20%D1%87%D1%91%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C%C2%BB)
    
* [Калькулятор.](https://github.com/EvgenyAleksov/python-project-49/edit/main/README.md#%D0%B8%D0%B3%D1%80%D0%B0-%D0%BA%D0%B0%D0%BB%D1%8C%D0%BA%D1%83%D0%BB%D1%8F%D1%82%D0%BE%D1%80:~:text=%D0%98%D0%B3%D1%80%D0%B0-,%22%D0%9A%D0%B0%D0%BB%D1%8C%D0%BA%D1%83%D0%BB%D1%8F%D1%82%D0%BE%D1%80%22,-%D0%9F%D0%BE%D0%BA%D0%B0%D0%B7%D1%8B%D0%B2%D0%B0%D0%B5%D1%82%D1%81%D1%8F%20%D1%81%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%BE%D0%B5%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5)
Арифметические выражения, которые необходимо вычислить.

* [Наибольший общий делитель (НОД).](https://github.com/EvgenyAleksov/python-project-49/edit/main/README.md#%D0%B8%D0%B3%D1%80%D0%B0-%D0%BA%D0%B0%D0%BB%D1%8C%D0%BA%D1%83%D0%BB%D1%8F%D1%82%D0%BE%D1%80:~:text=%22%D0%9D%D0%B0%D0%B8%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B8%D0%B9%20%D0%BE%D0%B1%D1%89%D0%B8%D0%B9%20%D0%B4%D0%B5%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%20(%D0%9D%D0%9E%D0%94)%22)
Определение наибольшего общего делителя.

* [Арифметическая прогрессия.](https://github.com/EvgenyAleksov/python-project-49/edit/main/README.md#%D0%B8%D0%B3%D1%80%D0%B0-%D0%BA%D0%B0%D0%BB%D1%8C%D0%BA%D1%83%D0%BB%D1%8F%D1%82%D0%BE%D1%80:~:text=%C2%AB%D0%90%D1%80%D0%B8%D1%84%D0%BC%D0%B5%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D1%8F%C2%BB)
Поиск пропущенных чисел в последовательности чисел.

* [Простое ли число?](https://github.com/EvgenyAleksov/python-project-49/edit/main/README.md#%D0%B8%D0%B3%D1%80%D0%B0-%D0%BA%D0%B0%D0%BB%D1%8C%D0%BA%D1%83%D0%BB%D1%8F%D1%82%D0%BE%D1%80:~:text=%D0%98%D0%B3%D1%80%D0%B0-,%C2%AB%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B5%20%D0%BB%D0%B8%20%D1%87%D0%B8%D1%81%D0%BB%D0%BE%3F%C2%BB,-%D0%9F%D0%BE%D0%BA%D0%B0%D0%B7%D1%8B%D0%B2%D0%B0%D0%B5%D1%82%D1%81%D1%8F%20%D1%81%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%BE%D0%B5%20%D1%87%D0%B8%D1%81%D0%BB%D0%BE)
Определение простого числа. 
  

## Игра «Проверка на чётность»
Показывается случайное число.
Нужно ответить yes, если число чётное, и no - если нет.

**Запуск**
```
$ brain-even
```

_Пример_

[![asciicast](https://asciinema.org/a/yziIELOXd2UKsSf2kejL6DrDi.svg)](https://asciinema.org/a/yziIELOXd2UKsSf2kejL6DrDi)


## Игра "Калькулятор"
Показывается случайное математическое выражение, например 35 + 16, которое нужно вычислить и записать правильный ответ.

**Запуск**
```
$ brain-calc
```

_Пример_

[![asciicast](https://asciinema.org/a/enJSpsEAVdWmwPUTWyEEcFXXT.svg)](https://asciinema.org/a/enJSpsEAVdWmwPUTWyEEcFXXT)


## Игра "Наибольший общий делитель (НОД)"
Показываются два случайных числа, например, 25 и 50.
Нужно вычислить и ввести наибольший общий делитель этих чисел.

**Запуск**
```
$ brain-gcd
```

_Пример_

[![asciicast](https://asciinema.org/a/Sn307pUZ00jLQeHPggeu3EO35.svg)](https://asciinema.org/a/Sn307pUZ00jLQeHPggeu3EO35)


## Игра «Арифметическая прогрессия»
Показывается ряд чисел, который образует арифметическую прогрессию.
Одно (любое) из чисел заменено двумя точками.
Нужно определить это число.

**Запуск**
```
$ brain-progression
```

_Пример_

[![asciicast](https://asciinema.org/a/W0I29PozhRv6HxO2LpeaUGnxZ.svg)](https://asciinema.org/a/W0I29PozhRv6HxO2LpeaUGnxZ)


## Игра «Простое ли число?»
Показывается случайное число.
Нужно ответить yes, если число простое, и no — если нет.

**Запуск**
```
$ brain-prime
```

_Пример_

[![asciicast](https://asciinema.org/a/bdlqQsmKVwKcr1ib1SvpFYZuf.svg)](https://asciinema.org/a/bdlqQsmKVwKcr1ib1SvpFYZuf)


## Требования к установке
```
* Python 3.10.
* Poetry 1.8
```


## Установка
Для запуска игр необходимо предварительно установить данный проект.

1. Склонировать репозиторий:
```
$ https://github.com/EvgenyAleksov/python-project-49.git
```

2. Установить проект:
```
$ make package-install
````


**Команды зля запуска каждой игры указаны преред примерами выше.**


## Проверка кода проекта линтером _flake8_
```
$ poetry run flake8 brain_games
```
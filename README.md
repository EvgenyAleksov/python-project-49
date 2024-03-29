### Hexlet tests and linter status:
[![Actions Status](https://github.com/EvgenyAleksov/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/EvgenyAleksov/python-project-49/actions)


[![Maintainability](https://api.codeclimate.com/v1/badges/da1d813750c6909348f7/maintainability)](https://codeclimate.com/github/EvgenyAleksov/python-project-49/maintainability)


# Проект Игры разума
**«Игры разума»** — набор из пяти консольных игр.
Каждая игра задает вопросы, на которые нужно дать правильные ответы.
Игра считается пройденной после трёх правильных ответов.
Неправильный ответ на любом шаге завершает игру, после чего предлагается пройти её заново.


**Игры:**

* [Проверка на чётность.](#игра-проверка-на-чётность)
    
* [Калькулятор.](#игра-калькулятор)
Арифметические выражения, которые необходимо вычислить.

* [Наибольший общий делитель (НОД).](#игра-наибольший-общий-делитель-нод)
Определение наибольшего общего делителя.

* [Арифметическая прогрессия.](#игра-арифметическая-прогрессия)
Поиск пропущенных чисел в последовательности чисел.

* [Простое ли число?](#игра-простое-ли-число)
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
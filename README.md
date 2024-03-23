### Hexlet tests and linter status:
[![Actions Status](https://github.com/EvgenyAleksov/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/EvgenyAleksov/python-project-49/actions)


[![Maintainability](https://api.codeclimate.com/v1/badges/da1d813750c6909348f7/maintainability)](https://codeclimate.com/github/EvgenyAleksov/python-project-49/maintainability)


<p>&nbsp;</p>
<p>&nbsp;</p>
<p>Проект <strong>Игры разума</strong><br /><br /><strong>&laquo;Игры разума&raquo;</strong> &mdash; набор из пяти консольных игр.<br />Каждая игра задает вопросы, на которые нужно дать правильные ответы.<br />Игра считается пройденной после трёх правильных ответов.<br />Неправильный ответ на любом шаге завершает игру, после чего предлагается пройти её заново.<br /><br /></p>
<p>&nbsp;</p>
<p><strong>Игры:</strong></p>
<ul>
<li>Проверка на чётность.<br /><br /></li>
<li>Калькулятор.<br />Арифметические выражения, которые необходимо вычислить.<br /><br /></li>
<li>Наибольший общий делитель (НОД).<br />Определение наибольшего общего делителя.<br /><br /></li>
<li>Арифметическая прогрессия.<br />Поиск пропущенных чисел в последовательности чисел.<br /><br /></li>
<li>Простое ли число?<br />Определение простого числа.&nbsp;</li>
</ul>
<p>&nbsp;</p>
<p><br />Игра <strong>&laquo;Проверка на чётность&raquo;</strong></p>
<p>Показывается случайное число.<br />Нужно ответить <strong>yes</strong>, если число чётное, и <strong>no</strong>&nbsp;- если нет.</p>
<p><em>Запуск</em></p>
<p>```bash</p>
<p>$ brain-even</p>
<p>```</p>
<p><em>Пример</em></p>
<p>[![asciicast](https://asciinema.org/a/yziIELOXd2UKsSf2kejL6DrDi.svg)](https://asciinema.org/a/yziIELOXd2UKsSf2kejL6DrDi)</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>Игра <strong>"Калькулятор"</strong></p>
<p>Показывается случайное математическое выражение, например 35 + 16, которое нужно вычислить и записать правильный ответ.</p>
<p><em>Запуск</em></p>
<p>```bash</p>
<p>$ brain-calc</p>
<p>```</p>
<p><em>Пример</em></p>
<p>[![asciicast](https://asciinema.org/a/enJSpsEAVdWmwPUTWyEEcFXXT.svg)](https://asciinema.org/a/enJSpsEAVdWmwPUTWyEEcFXXT)</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>Игра <strong>"Наибольший общий делитель (НОД)"</strong></p>
<p>Показываются два случайных числа, например, 25 и 50.<br />Нужно вычислить и ввести наибольший общий делитель этих чисел.</p>
<p><em>Запуск</em></p>
<p>```bash</p>
<p>$ brain-gcd</p>
<p>```</p>
<p><em>Пример</em></p>
<p>[![asciicast](https://asciinema.org/a/Sn307pUZ00jLQeHPggeu3EO35.svg)](https://asciinema.org/a/Sn307pUZ00jLQeHPggeu3EO35)</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>Игра <strong>&laquo;Арифметическая прогрессия&raquo;</strong></p>
<p>Показывается ряд чисел, который образует арифметическую прогрессию.<br />Одно (любое) из чисел заменено двумя точками.<br />Нужно определить это число.</p>
<p><em>Запуск</em></p>
<p>```bash</p>
<p>$ brain-progression</p>
<p><em><strong></strong></em>```</p>
<p><em>Пример</em></p>
<p>[![asciicast](https://asciinema.org/a/W0I29PozhRv6HxO2LpeaUGnxZ.svg)](https://asciinema.org/a/W0I29PozhRv6HxO2LpeaUGnxZ)</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>Игра <strong>&laquo;Простое ли число?&raquo;</strong></p>
<p>Показывается случайное число.<br />Нужно ответить yes, если число простое, и no &mdash; если нет.</p>
<p><em>Запуск</em></p>
<p>```bash</p>
<p>$ brain-prime</p>
<p>```</p>
<p><em>Пример</em></p>
<p>[![asciicast](https://asciinema.org/a/bdlqQsmKVwKcr1ib1SvpFYZuf.svg)](https://asciinema.org/a/bdlqQsmKVwKcr1ib1SvpFYZuf)</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><strong>Требования к установке</strong></p>
<p>```bash</p>
<ul>
<li>Python 3.10.<br /><br /></li>
<li>Poetry 1.8</li>
</ul>
<p>```</p>
<p>&nbsp;</p>
<p><strong>Установка</strong></p>
<p>Для запуска игр необходимо предварительно установить данный проект:<br /><br />1. Склонировать репозиторий:</p>
<p>```bash</p>
<p>$ https://github.com/EvgenyAleksov/python-project-49.git</p>
<p>```</p>
<p>&nbsp;</p>
<p>2. Установить проект:</p>
<p>```bash</p>
<p>$ make package-install</p>
<p>````</p>
<p>&nbsp;</p>
<p>Команды зля запуска каждой игры указаны преред примерами выше.&nbsp;</p>
<p>&nbsp;</p>
<p><strong>Проверка кода проекта линтером&nbsp;<em>flake8</em><br /></strong></p>
<p>```bash</p>
<p>poetry run flake8 brain_games</p>
<p><strong>```</strong></p>
<p>&nbsp;</p>

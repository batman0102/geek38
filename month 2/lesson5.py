# модули - встроенные, собственные, внешние
# venv - виртуальная среда

#внешние модули
#зависимости - все, что мы устанавливаем в venv
#библиотека - и модуль и зависимость (сборище пайтон пакетов)
#фреймворк - библиотека, но нельзя писать где угодно
from art import tprint
tprint('Hello World')

import colorama
print(colorama.Back.RED)
print(colorama.Fore.BLACK)
tprint('HELLO WORLD')

import random
print(random.randint(1,9))



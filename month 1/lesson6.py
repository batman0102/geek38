#Функции, агрументы: *args, *kwargs

# length = 7
# width = 5
# square_2 = length*width
# print(square_2)
#
# length = 200
# width = 250
# square_victory = length*width
# print(square_victory)

#DRY - не повторяйся

'''схема функции'''
# определение наименование(параметры):
#      тело функции
#      возврашение функции
#
# вызов функции
# наименование(агрументы)

# def get_data():
#     print('Hello')
#
# get_data()

# def get_data(name, surname):   #name - обязательный позиционный параметр
#     print(f'name:{name} surname:{surname}')
#
# get_data("ruslan", 'tursunaliev')   #обязательный позиционный аргумент

# def get_data(name, surname = 'unknown'):   #surname = необязательный позиционный параметр
#     print(f'name:{name} surname:{surname}')
#
# get_data("ruslan", 'tursunaliev')
# get_data('anya')
# get_data('asanov', 'tilek') #нужно учитывать их позиции, но
# get_data(surname ='asanov', name = 'tilek') #ключевые аргументы

'''возвращение функции'''

# word = 'python'
# counter = 0
# for i in word:
#     counter += 1
#
# print(counter)

# word = 'Kyrgyzstan'
# def len1(iterable):
#     counter = 0
#     for i in iterable:
#         counter += 1
#     return counter
#
# print(len1(word))
# print(len(word))

# def get_square(length , width):
#     return length*width
#
# square_2 = get_square(7,5)
# square_hall = get_square(10,15)
#
# print(square_2)
# print(square_hall)

# length = 7
# width = 5
# square_2 = length*width
# print(square_2)
#
# length = 200
# width = 250
# square_victory = length*width
# print(square_victory)

# def get_square(length: int , width: int) -> int:
#     """принимает длину/ширину и возвращает площадь"""
#     return length*width
# print(help(get_square))

# print(len.__doc__)
# print(help(len))

# def plus(num1,num2):
#     return num1 + num2
#
#  print(plus(6,8))


# def plus(*args):
#     return sum(args)

# print(plus(12,14,15,156))

word = 'Kyrgyzstan'
# def len1(iterable):
#     counter = 0
#     for i in iterable:
#         counter += 1
#     return counter
#
# print(len1(word))
# print(len1('word'))
# print(len1(['1', '2', '3']))

def sum1(iterable):
    total = 0
    for number in iterable:
        total += number
    return total

numbers = (3, 7, 1, 4, 6, 8, 2, 5)
print(sum1(numbers))



# print(help(sum))
# """lambda function"""
# # lambda arguments: expression
# # filter, sorted, map

# numbers = [996, 312, 1991, 2010, 3138]
#
# mapped_numbers = list(map(lambda i: i + 100, numbers))
# print(mapped_numbers)
#
# filtered_numbers = list(filter(lambda i: i>1000, numbers))
# print(filtered_numbers)

# names = ['azamat', 'erlan', 'samat', 'uluk']
# print(names)
#
# mapped_names = list(map(lambda n: n.upper(), names))
# print(mapped_names)
#
# filtered_names = list(filter(lambda n: len(n) <= 5, names))
# print(filtered_names)

# sorted_names = sorted(names, key=lambda x: x[1])
# print(sorted_names)


# lambda_f = lambda num1, num2: num1 + num2
# print(lambda_f(2, 4))
#
#
# def def_f(num1, num2):
#     return num1 + num2
# print(def_f(3, 3))

# def up_letter(word: str):
#     return word.title()


# def show_words(func, iterable):
#     for i in iterable:
#         print(func(i))

# show_words(lambda word: word.title(), ['bishkek', 'naryn', 'balykchy'])
# show_words(str.upper, ['kg', 'kz', 'ru'])
# show_words(len, ('2463', '45645', '43234', '98087', '34591'))
# show_words(up_letter, ['tokmok', 'karakol', 'kant'])

"""исключения"""
# try:
#     code
# except:
#     code
#     message
# finally:
#     message
#     code

# try:
#     print('python'[2])
# except:
#     print('нашли ошибку!')
# finally:
#     print('проверка завершена')

# print(int('b'))
# print(4 + 'l') 
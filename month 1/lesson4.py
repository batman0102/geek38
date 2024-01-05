"""встроенная функция list()"""

# students = ['ilziya', 'ayana', 'ibragim', 'dmitriy', 'syimyk']
# print(type(students))
# print(list(range(1,11)))

students2 = ['bekbol', 'bekzat']
students = ['ilziya', 'ayana', 'ibragim', 'dmitriy', 'syimyk']


# print(students[2:5])
# print(students[1])


"""добавление"""
# students.append('bekbolsun')
# print(students)
# students.insert(1, 'ruslan')
# print(students)
# students.extend(students2)
# print(students)

"""изменение"""
# students[1] = 'aiana'
# students[0],students[1] = students[1], students[0]
# students[:2] = students2
# students.sort(reverse=True)
# students.reverse()

"""удаление"""
students.remove('ibragim')
print(students)
deleted = students.pop(2)
print(students)
del students[0:3]
print(students)

"""list comprehension"""
# students = ['ilziya', 'ayana', 'ibragim', 'dmitriy', 'syimyk']
# students=[student for student in students if student != 'ibragim']
# students=[student for student in students if student.startswith('i')]
# print(students)

"""sum,max.min,len"""
# numbers = [4, 2, 7.3, 5.8, 1, 6, 99]
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))
# print(len(numbers))

# cities = ('tokmok', 'bishkek', 'osh', 'kara-balta')
# cities = list(cities)
# cities = tuple(cities)
# print(type(cities))
# print(cities)

# expenses = [int(input(f'введите расход за день: {i})')) for i in range(1,8)]
# print(sum(expenses) / len(expenses))

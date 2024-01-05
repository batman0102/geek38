'''словари - dict'''  '''set - множество'''
# student = ['azamat', 'urmat', 'karina']
# {key: value}
# print(student['name'])
# print(student['age'])

"""что может делать dict"""
# print(dict(enumerate('python')))
new = dict(name='Azamat', age=20, country='KG')
# print(new)
student = {
    'name': 'Jack',
    'surname': 'Walker',
    'age': 19
}
""""как может изменяться словарь"""

""""добавление"""

# student['height'] = 1.76
# student['married'] = False
# student['hobby'] = ['english', 'chess', 'books']

"""изменение"""

# student['age'] += 1
# student['name'] = 'John'
# student.update(new)

"""удаление"""

# del student['surname']
# student.pop('age')

# for i in student:
#     print(i, student[i])

# print(student.keys())
# print(student.values())
# print(student.items())

for key, value in student.items():
    print(key, ':', value)

# expenses = {i: int(input(f'enter exp: for {i}')) for i in range(1, 8)}
#
# for day, expense in expenses.items():
#     print(f"{day} : {expense}")
#
# print(sum(expenses.values())/ len(expenses))

# numbers = [1, 2, 3, 2, 1, 4, 5, 3]
numbers2 = {1, 2, 3, 2, 1, 4, 5, 3}
# print(numbers)
print(numbers2)

# lagman = {'лапша', 'мясо', 'перец'}
# manty = {'тесто', 'мясо', 'лук'}
#
# print(lagman.symmetric_difference(manty))
# print(lagman.difference(manty))
# print(lagman.union(manty))
# print(lagman.intersection(manty))







# print(student)




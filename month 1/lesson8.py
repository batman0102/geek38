#w-write (запись, перезапись)
#a-add (дозапись)
#x-создание файла без повторения имен
#r-read (чтение)

# file=open('new_file.txt', 'w', encoding='utf-8')
# file.write('Бишкек, ГИКС')
# file.close()

# with open('new_file.txt', 'a', encoding='utf-8') as file:
#     file.write("\nвторая строка2!")
#
# with open('new_file.txt', 'w', encoding='utf-8') as file:
#     file.write("\nвторая строка2!")
#
# with open('new_file1.txt', 'x', encoding='utf-8') as new_file:
#     new_file.write('123')

# from time import sleep
#
# with open('new_file.txt', 'r', encoding='utf-8') as file:
#     for i in file.read():
#         sleep(1)
#         print(i, end='')


# print(file.read()[0])
# print(file.readlines())

# from random import choice
#
# students = [11, 10, 3, 13, 7, 1, 4]
# topics = tuple(range(1, 8))
#
# with open('results.txt', 'w', encoding='utf-8') as new_file:
#     new_file.write('38-3 RESULTS\n')
#
# while students:
#     chosen_students = choice(students)
#     name = input(f'enter name for {chosen_students}: ').title()
#     rate = input(f"topic: {choice(topics)}\n enter rate for {name}: ")
#     with open('results.txt', 'a', encoding='utf-8') as file:
#         file.write(f'\n{name} - {rate}')
#     students.remove(chosen_students)
#     print(f"студентов осталось: {students}")


with open('results.txt', encoding='utf-8') as file:
    file.readline()
    file.readline()
    print(file.readlines())


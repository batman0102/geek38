#Расширить функцию “Ближайшее Число”
number_list = (345, 600, 999, 56, 13445)
number = 500

def nearest_number(number, number_list):
    sorted_numbers = sorted(number_list, key = lambda x: (x - number)**2)
    return (number, sorted_numbers)

result = nearest_number(number, number_list)
print (result)



# 3) Напишите примеры использования lambda функций с такими функциями как filter, map по одному примеру на своё усмотрение

numbers = [996, 312, 1991, 2010, 3138]

mapped_numbers = list(map(lambda i: i + 100, numbers))
print(mapped_numbers)

filtered_numbers = list(filter(lambda n: n>1000, numbers))
print(filtered_numbers)



# 2) Создать функцию для вывода элемента списка/кортежа/строки (iterable) по указанному индексу.
my_list = (10, 43, 56, 100, 258)

def det_element (iterable):
    while True:
        index_in = input('enter index or b')
        if index_in == 'b':
            break
        else:
            try:
                index_in = int(index_in)
                print(my_list[index_in])
            except ValueError:
                print("Введите целочисленное значение индекса.")
            except IndexError:
                print(f'Индекс вне диапазона. Введите индекс от 0 до {len(iterable) - 1}')

print(det_element(my_list))

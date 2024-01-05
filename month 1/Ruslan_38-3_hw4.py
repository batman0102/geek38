mentors = ["Кубаныч", "Мирлан", "Гулина", "Камиля"]
while True:
    print("Список менторов:")
    for mentor in mentors:
        print(mentor)

    print("Выберите команду:")
    print("1) Добавить ментора")
    print("2) Заменить ментора")
    print("3) Удалить ментора")
    print("4) Выход")

    command = input("Введите номер команды: ")
    if command == "1":
        name = input('Введите имя ментора для добавления:').capitalize()
        if len(name) <= 15 and name not in mentors:
            mentors.append(name)
            print("Имя добавлено в список менторов!")
        elif len(name) > 15:
            print("Имя должно содержать не более 15 символов!")
        else:
            print("Имя уже есть в списке!")
    elif command == "2":
        old_name = input("Введите имя ментора для замены:").capitalize()
        if old_name in mentors:
            new_name = input("Введите новое имя ментора:").capitalize()
            if len(new_name) <= 15 and new_name not in mentors:
                mentors[mentors.index(old_name)] = new_name
                print(f"Имя ментора {old_name} успешно заменено на {new_name}.")
            elif len(new_name) > 15:
                print("Имя должно содержать не более 15 символов!")
            else:
                print("Имя уже есть в списке!")
    elif command == "3":
        print("Удалять ментора можно по имени и индексу.")
        print("Выберите команду:")
        print("1) Удалить по имени")
        print("2) Удалить по индексу")

        command1 = input("Выберите номер команды:")

        if command1 == "1":
            name = input("Введите имя ментора для удаления:").capitalize()
            if name in mentors:
                mentors.remove(name)
                print(f"Ментор {name} был удален!")
            else:
                print("Такого имени нет в списке!")
        elif command1 == "2":
            index = int(input("Введите индекс ментора для удаления:"))
            if index <= 3:
                del mentors[index]
                print(f"Ментор с индексом {index} успешно удален.")
            else:
                print("Некорректный ввод.")
        else:
            print("Некорректный ввод.")

    elif command == "4":
        break
    else:
        print("Некорректная команда. Попробуйте еще раз.")

mentors = (tuple(mentors))
print("Финальный список менторов в виде кортежа:")
print(mentors)












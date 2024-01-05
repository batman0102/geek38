def guess_number():
    low, high = 1, 100
    attempts = 0
    attempts_list = []

    secret_number = int(input("Загадайте число от 1 до 100: "))
    if secret_number >= 1 and secret_number <= 100:
        while True:
            guess = (low + high) // 2
            attempts += 1
            attempts_list.append(guess)

            print(f"Это число {guess}?")
            user_input = input("Введите 1 (да), 2 (больше), 3 (меньше): ")

            if user_input == '1':
                print(f"Программа угадала ваше число {guess} за {attempts} попыток.")

                with open("results.txt", "w", encoding='utf-8') as file:
                    file.write(f"Загаданное число: {secret_number}\n")
                    file.write(f"Число программы: {guess}\n")
                    file.write(f"Попыток: {attempts}\n")
                    file.write(f"Список попыток: {attempts_list}\n")

                break
            elif user_input == '2':
                low = guess + 1
            elif user_input == '3':
                high = guess - 1
            else:
                print("Некорректный ввод. Введите 1 (да), 2 (больше), 3 (меньше).")
    else:
        print("Введите число от 1 до 100!")

print(guess_number())

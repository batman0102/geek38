while True:
    word = input("Введите любое слово на латинице или кириллице или введите 'stop' при выходе:")

    if word.lower()=="stop":
        break

    total_letters = len(word)
    vowels = 0
    consonants = 0

    for letter in word:
        if letter.lower() in 'aeyiouаеёиоуыэюя':
            vowels += 1
        elif letter.lower() in 'qwrtpsdfghjklzxcvbnmйцкнгшщзхфвпрлджчсмтб':
            consonants += 1

    if total_letters > 0:
        vowels_percentage = (vowels / total_letters) * 100
        consonants_percentage = (consonants / total_letters) * 100
        print(f"Слово: {word}")
        print(f"Количество букв: {total_letters}")
        print(f"Гласных букв: {vowels}")
        print(f"Согласных букв: {consonants}")
        print (f"Гласные/Согласные: {'%.2f'%vowels_percentage} / {'%.2f'%consonants_percentage}")
    else:
        print ("Слово не содержит букв.")


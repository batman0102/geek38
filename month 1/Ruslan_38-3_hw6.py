
movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    },
    "Troy": {}
}

while True:
    print("1. Добавить фильм")
    print("2. Добавить рейтинг к фильму")
    print("3. Просмотреть рейтинги для всех фильмов")
    print("4. Список фильмов")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        movie_name = input("Введите название фильма: ").title()

        if movie_name in movies:
            print("This movie already exists!")
        else:
            movies[movie_name] = {}
            print("Movie added successfully")
    elif choice == "2":
        movie2_name = input("Введите название фильма: ").title()
        if movie2_name not in movies:
            print("This movie doesn't exist")
        else:
            name = input("Введите ваше имя:").title()
            rating = int(input("Введите оценку фильма от 1 до 10:"))
            if rating >= 0 and rating <= 10:
                movies[movie2_name][name] = rating
                print(f"A rating has been added for {movie2_name}: {name} rated it {rating}")
            else:
                print("Неправильно введена оценка")
    elif choice == "3":
        for movie, rating in movies.items():
            if not rating:
                print(f"Rating is not yet available for {movie}")
            else:
                average_rating = sum(rating.values()) / len(rating)
                print(f"{movie} is rated {average_rating:.1f}")
    elif choice == "4":
        print(movies)
    elif choice == "5":
        break
    else:
        print("Некорректный выбор.")













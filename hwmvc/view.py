def add_name(name):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {name} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_name(" Редактирование данных каталога фильмов ")
    def wait_user_answer(self):
        # print(" Редактирование данных каталога фильмов ".center(50, "="))
        print(" Деиствия с фильмами: ")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов "
              "\n3 - Просмотр определенного фильма"
              "\n4 - Удаление фильма"
              "\nk - выход из программы ")
        user_answer = input("Выберите вариант деиствия : ")
        # print("=" * 50)
        return user_answer

    @add_name(" Добавление фильма ")
    def add_user_film(self):
        dict_film = {
            "название": None,
            "жанр": None,
            "режиссера": None,
            "год выпуска": None,
            "длительность": None,
            "студию": None,
            "актеров": None
        }
        # print(" Добавление фильма ".center(50, "="))
        for key in dict_film:
            dict_film[key] = input(f"Введите {key} фильма : ")
        # print("=" * 50)
        return dict_film

    @add_name("Список фильмов ")
    def show_all_films(self, films):
        # print(" Список фильмов ".center(50, "="))
        for ind, film in enumerate(films, 1):
            print(f"{ind}. {film}")
        # print("=" * 50)

    @add_name(" Ввод определенного фильма ")
    def get_user_film(self):
        user_film = input(" Введите название фильма :")
        return user_film

    @add_name(" Просмотр определенного фильма ")
    def show_single_film(self, film):
        for key in film:
            print(f" {key} статьи = {film[key]}")

    @add_name(" Сообщение об ошибке ")
    def show_incorrect_name_error(self, film_name):
        print(f"статья с названием {film_name} не существует")

    @add_name(" Удаление статьи ")
    def remove_single_film(self, film):
        print(f"Статья {film} - была удалена")

    @add_name("  ")
    def show_incorrect_answer_error(self, answer):
        print(f" Варианта с {answer} не существует")

def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    return wrapper

class UserUnterface:
    @add_title(" Ввод пользовательских данных ")
    def wait_user_answer(self):
        # print(" Ввод пользовательских данных ".center(50, "="))
        print("Деиствие со статьями:")
        print("1 - создание статьи"
              "\n2 - просмотр статеи"
              "\n3  просмотр определеннои статьи"
              "\n4 - удаление статьи"
              "\nk - выход из программы")
        user_answer = input("Выбрать вариант деиствия:")
        # print("=" * 50)
        return user_answer

    @add_title(" Введите название статьи ")
    def add_user_article(self):
        dict_article = {
            "название": None,
            "автора": None,
            "количество страниц": None,
            "описание": None
            }
        # print("Создание статьи ".center(50, "="))
        for key in dict_article:
            dict_article[key] = input(f"Введите {key} статьи: ")
        # print("=" * 50)
        return dict_article

    @add_title(" Список статеи ")
    def show_all_articles(self, articles):
        # print(" Список статеи ".center(50, "="))
        for ind, article in enumerate(articles, 1):
            print(f"{ind}. {article}")
        # print("=" * 50)

    @add_title(" Ввод названия статьи ")
    def get_user_article(self):
        user_article = input("Введите название статьи")
        return user_article


    @add_title(" Просмотр статьи ")
    def show_single_article(selfself, article):
        for key in article:
            print(f"{key} статьи - {article[key]}")

    @add_title("Сообщение об ошибке ")
    def show_incorrect_title_error(self, user_title):
        print(f"Статья с названием {user_title} не существует")

    @add_title("Delete статьи ")
    def remove_single_article(self, article):
        print(f" Статья {article} - была удалена")

    @add_title("Сообщ об ошибке ")
    def show_incorrect_answer_error(self, answer):
        print(f" Варианта {answer} не существует")
class UserUnterface:
    def wait_user_answer(self):
        print(" Ввод пользовательских данных ".center(50, "="))
        print("Деиствие со статьями:")
        print("k - выход из программы")
        user_answer = input("Выбрать вариант деиствия:")
        print("=" * 50)
        return user_answer

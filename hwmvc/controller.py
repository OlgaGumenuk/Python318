from view import UserInterface
from model import FilmModel

class Controller:
    def __init__(self):
        self.film_model = FilmModel()  # model
        self.user_interface = UserInterface()  # view

    def run(self):
        answer = None
        while answer != "k":
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            film = self.user_interface.add_user_film()
            self.film_model.add_film(film)
        elif answer == "2":
            film = self.film_model.get_all_films()
            self.user_interface.show_all_films(film)
        elif answer == "3":
            film_name = self.user_interface.get_user_film()
            try:
                film = self.film_model.get_single_film(film_name)
            except KeyError:
                self.user_interface.show_incorrect_name_error(film_name)
            else:
                self.user_interface.show_single_film(film)
        elif answer == "4":
            film_name = self.user_interface.get_user_film()
            try:
                name = self.film_model.remove_film(film_name)
            except KeyError:
                self.user_interface.show_incorrect_name_error(film_name)
            else:
                self.user_interface.remove_single_film(name)
        elif answer == "k":
            self.film_model.save_data()
        else:
            self.user_interface.show_incorrect_answer_error(answer)



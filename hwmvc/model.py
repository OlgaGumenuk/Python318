import pickle
import os.path

class Film:
    def __init__(self, name, genre, maker, born, time, studio, actors):
        self.name = name
        self.genre = genre
        self.maker = maker
        self.born = born
        self.time = time
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.name} ({self.maker})"


class FilmModel:
    def __init__(self):
        self.db_name = "dbhw.txt"
        self.films = self.load_data()

    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.films[film.name] = film

    def get_all_films(self):
        return self.films.values()

    def get_single_film(self, user_name):
        film = self.films[user_name]
        dict_film = {
            "название": film.name,
            "жанр": film.genre,
            "режиссера": film.maker,
            "год выпуска": film.born,
            "длительность": film.time,
            "студию": film.studio,
            "актеров": film.actors
        }
        return dict_film

    def remove_film(self, user_name):
        return self.films.pop(user_name)

    def save_data(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.films, f)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()










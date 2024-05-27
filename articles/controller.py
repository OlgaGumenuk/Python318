from view import UserUnterface
class Controller:
    def __init__(self):
        self.article_model = None  # model
        self.user_interface = UserUnterface()  # view

    def run(self):
        answer = None
        while answer != "k":
            answer = self.user_interface.wait_user_answer()


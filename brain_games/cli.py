import prompt


class Cli:
    def __init__(self):
        print("Welcome to Brain Games!")
        self.user_name = "Anonymous"

    def ask_name(self):
        self.user_name = prompt.string("May I have your name? ")

    def welcome(self):
        print(f"Hello, {self.user_name}!")

    def congrats(self):
        print(f"Congratulations, {self.user_name}!")

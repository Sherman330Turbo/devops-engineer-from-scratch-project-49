import prompt


def ask_name() -> str:
    return prompt.string("May I have your name? ")


def welcome_user(user_name):
    print(f"Hello, {user_name}!")


def congrats(user_name):
    print(f"Congratulations, {user_name}!")

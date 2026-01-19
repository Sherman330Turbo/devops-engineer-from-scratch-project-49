import prompt


def get_user_name():
    return prompt.string("May I have your name? ")


def welcome_user(user_name: str = None):
    print(f"Hello, {get_user_name() if user_name is None else user_name}!")


def congrats_user(user_name: str = None):
    print(f"Congratulations{'' if user_name is None else f', {user_name}'}!")

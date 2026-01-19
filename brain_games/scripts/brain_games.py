from brain_games.cli import welcome_user


# file: my_application/module.py
def greet():
    print('Welcome to the Brain Games!')
    welcome_user()


def main():
    greet()
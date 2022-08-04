import random

NAME_1 = "John"
NAME_2 = "Jack"


def is_numeric(number: str) -> int:
    while not number.isdigit():
        number = input("The number of pencils should be numeric\n")
    return int(number)


def is_positive(number: int) -> int:
    while number <= 0:
        number = input("The number of pencils should be positive\n")
        number = is_numeric(number)
    return number


def players_name() -> str:
    name = input("Who will be the first (" + NAME_1 + ", " + NAME_2 + "):\n")
    while name not in (NAME_1, NAME_2):
        name = input("Choose between '" + NAME_1 + "' and '" + NAME_2 + "'\n")
    return name


def print_turn(number: int, name: str) -> None:
    print("|" * number)
    print(name + "'s turn!")
    

def number_pencils(value: str) -> int:
    while value not in ("1", "2", "3"):
        value = input("Possible values: '1', '2' or '3'\n")
    return int(value)


def start_game() -> (int, int):
    number = input("How many pencils would you like to use:\n")
    number = is_numeric(number)
    number = is_positive(number)
    name = players_name()
    turn = 0 if name == NAME_1 else 1
    return number, turn


def is_valid(value: int, number: int) -> int:
    while value > number:
        value = input("Too many pencils were taken\n")
        value = number_pencils(value)
    return value


def winning_strategy(n: int) -> int:
    return (n - 1) % 4


def bot_play(number: int) -> int:
    winning = winning_strategy(number)
    if winning:
        return winning
    return random.randint(1, min(number, 3))


def main():
    names = (NAME_1, NAME_2)
    number, turn = start_game()
    while number > 0:
        name = names[turn]
        print_turn(number, name)
        if turn == 0:
            num_pencils = number_pencils(input())
            num_pencils = is_valid(num_pencils, number)
        else:
            num_pencils = bot_play(number)
            print(num_pencils)
        number -= num_pencils
        turn = (turn + 1) % 2
    print(names[turn], "won!")


if __name__ == "__main__":
    main()

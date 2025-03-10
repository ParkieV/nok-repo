from functools import reduce
from random import randint


def nod(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a


def nok_both(a, b):
    """Return lowest common multiple."""
    return a * b // nod(a, b)


def nok_all(*args):
    """Return lcm of args."""
    return reduce(nok_both, args)


def cli():
    print("Find the smallest common multiple of given numbers.")
    num_tuple = tuple(randint(1, 30) for _ in range(3))
    print(f"Question: {' '.join((str(x) for x in num_tuple))}")
    correct_answer = nok_all(*num_tuple)

    user_answer = int(input("Your answer: "))

    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(
            f"'{user_answer}' is wrong number ;(. Correct answer was '{correct_answer}'."
        )
        print("Let's try again, Sam!")


def loop():
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    while True:
        cli()
        user_choose = input("Would you like to play again? ")
        match user_choose:
            case "y":
                pass
            case "Y":
                pass
            case "Yes":
                pass
            case "n":
                print("Thanks for playing!")
                break
            case "N":
                print("Thanks for playing!")
                break
            case "No":
                print("Thanks for playing!")
                break
            case _:
                raise AssertionError("Invalid input!")


def main() -> None:
    loop()


if __name__ == "__main__":
    main()

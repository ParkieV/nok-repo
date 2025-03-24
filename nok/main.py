from functools import reduce
from random import randint

from core import choose_loop


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


def game_loop():
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


if __name__ == "__main__":
    choose_loop(input_output_interface=game_loop)

from random import randint

from core import choose_loop


def generate_sequence() -> (int, str):
    num_seq = []
    multiplicator = randint(1, 6)
    num = 1
    for _ in range(randint(0, 2)):
        num *= multiplicator
    length = randint(5, 13)
    for _ in range(length):
        num_seq.append(str(num))
        num *= multiplicator
    hidden_index = randint(0, length - 1)
    hidden_num = int(num_seq[hidden_index])
    num_seq[hidden_index] = ".."
    return hidden_num, " ".join(num_seq)


def game_loop() -> None:
    print("What number is missing in the progression?")
    hidden_num, question_string = generate_sequence()
    print(f"Question: {question_string}")
    correct_answer = hidden_num

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

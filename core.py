from collections.abc import Callable


def choose_loop(*, input_output_interface: Callable[[], None]) -> None:
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    while True:
        input_output_interface()
        user_choose = input("Would you like to play again? ")
        match user_choose:
            case _ if user_choose.lower() == "y":
                pass
            case _ if user_choose.lower() == "yes":
                pass
            case _ if user_choose.lower() == "n":
                print("Thanks for playing!")
                break
            case "N":
                print("Thanks for playing!")
                break
            case _ if user_choose.lower() == "no":
                print("Thanks for playing!")
                break
            case _:
                raise AssertionError("Invalid input!")

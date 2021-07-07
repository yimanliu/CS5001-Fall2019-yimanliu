import random

MAX_NUM = 20

maximum = int(input("Let's play a game. choose a number between 5 and {}: "
                    .format(MAX_NUM)))

if maximum < 5:
    print("goodbye")
    quit()
elif maximum > 20:
    print("goodbye")
    quit()

computer_choice = random.randint(0, maximum)


def evaluate_guess(computer_choice, player_guess):
    """Checks the computer choice with the player guess and ends the game if
    the guess is equal to computer_choice.

    >>> evaluate_guess(8, 3)
    too low
    -1

    """

    if player_guess < computer_choice:
        print("too low")
        return -1
    elif player_guess > computer_choice:
        print("too high")
        return 1
    else:
        print("you guess my number")
        return 0



guess = int(input("try number"))
if __name__ == "__main__":
    print(evaluate_guess(computer_choice, guess))

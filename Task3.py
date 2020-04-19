import random

game_over = False
guess_count = 0

try:

    print("This is a number guessing game. Select a game level:")
    game_levels = ['1 for Easy', '2 for Medium', '3 for Hard']
    for level in game_levels:
        print(level)
    selection = int(input(""))

    if selection == 1:
        correct_number = random.randint(1, 10)
        print("Guess a number between 1 and 10: ")
        guess_limit = 5
        while not game_over:
            guess = int(input("Guess: "))

            if guess == correct_number:
                print("That's correct! You win!!!")
                break

            elif guess != correct_number and guess_limit == 0:
                print("You failed to guess the number. Game Over!!")
                break
            else:
                guess_limit -= 1
                print(f"Wrong! You have {guess_limit + 1} guess(es) left")

    elif selection == 2:
        correct_number = random.randint(1, 20)
        print("Guess a number between 1 and 20:")
        guess_limit = 3

        while not game_over:
            guess = int(input("Guess: "))

            if guess == correct_number:
                print("That's correct! You win!!!")
                break
            elif guess != correct_number and guess_limit == 0:
                print("You failed to guess the number. Game Over!!")
                break
            else:
                guess_limit -= 1
                print(f"Wrong! You have {guess_limit + 1} guesses left")

    elif selection == 3:
        correct_number = random.randint(1, 50)
        print("Guess a number between 1 and 50:")
        guess_limit = 2

        while not game_over:
            guess = int(input("Guess: "))

            if guess == correct_number:
                print("That's correct! You win!!!")
                break
            elif guess != correct_number and guess_limit == 0:
                print("You failed to guess the number. Game Over!!")
                break
            else:
                guess_limit -= 1
                print(f"Wrong! You have {guess_limit + 1} guesses left")
    else:
        print(" Please select a number from above")
except ValueError:
    print("Please enter a number")
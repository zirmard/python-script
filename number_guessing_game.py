
import random

def guess_game():
    number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")

    while True:
        guess = int(input("Guess the number between 1 and 100: "))
        attempts += 1
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

guess_game()
    
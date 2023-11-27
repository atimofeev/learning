"""Number guessing game.

№1: 18 Python Projects for your Resume
"""
import random

secret_number = random.randint(1, 100)

attempts = 0

print("Guess random number 1-100")

while True:
    try:
        user_guess = int(input("> "))
        attempts += 1
        if user_guess > secret_number:
            print("Value too high")
        elif user_guess < secret_number:
            print("Value too low")
        elif user_guess == secret_number:
            print(
                f"Congratulations! Random number was {secret_number}. "
                f"You did it in {attempts} attempts"
            )
            break
    except ValueError:
        print("Provided value is not an integer.")
        continue

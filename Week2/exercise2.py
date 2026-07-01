"""
Problem 2: Guess the Number (with Exception Handling)
Write a program that asks the user to guess a secret number between 1 and 10.
The program should handle invalid inputs (non-numeric values) gracefully using
try/except and print helpful error messages.
The game ends when the user guesses the correct number.

Example:
Enter your guess: abc ➔ Invalid input. Please enter a number.
Enter your guess: 5 ➔ Too low!
Enter your guess: 10 ➔ Too high!
Enter your guess: 8 ➔ Correct! You win!
"""

import random
guess = 0

answer = random.randint(1, 10)
while guess != answer:
    try:
        guess = int(input("Enter your guess: "))

        if guess > 10 or guess < 1:
            print("Invalid input! Choose a number between 1 and 10.")
            continue

        if guess == answer:
            print("Correct! You win!")
            break

        if guess > answer:
            print("Too high!")
        elif guess < answer:
            print("Too low!")
    except ValueError as error:
        print("Invalid input! Please enter a number.")
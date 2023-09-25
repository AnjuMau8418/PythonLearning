# Number Guessing game between two numbers
import random
from NumberGuessing_art import logo

print(logo)
print('Welcome to the number Guessing Game!')
num1 = int(input("Enter starting number: "))
num2 = int(input("Enter ending number: "))
print(f"I am thinking of a number between {num1} and {num2}.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
if difficulty == 'hard':
    attempts = 5
else:
    attempts = 10

random_choice = random.randint(num1, num2)


def guessing_number(number_of_attempts):
    should_continue = True
    while should_continue:
        print(f"You have left {number_of_attempts} attempts remaining.")
        guess = int(input("Make a guess : "))
        if guess > random_choice:
            print("Too High")
        elif guess < random_choice:
            print(" Too low")
        else:
            print("You have guessed correct")
            break

        if number_of_attempts == 0:
            print("You have ran out of guesses, you lose.")
            should_continue = False
        else:
            print("Guess again")
            should_continue = True

        number_of_attempts -= 1


guessing_number(attempts)

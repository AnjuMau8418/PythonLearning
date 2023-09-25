# Hangman Game
import random
from Hangman_art import stages
from Hangman_words import word

print("Randomly choose a word:")
random_word = random.choice(word).lower()
print(f"The solution is {random_word}.")

num = len(random_word)
print(f"Chosen word length: {num}")

lives = 6

display = []
for _ in range(num):
    display += "_"

end_of_game = False
while not end_of_game:
    guess_letter = input("Guess a letter:").lower()

    if guess_letter in display:
        print(f"You have already guessed {guess_letter}.")
    for ch in range(num):
        letter = random_word[ch]
        if letter == guess_letter:
            display[ch] = letter

    print(display)
    if guess_letter not in random_word:
        print(f"You have guessed {guess_letter}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])

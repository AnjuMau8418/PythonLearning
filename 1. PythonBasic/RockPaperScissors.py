# Rock Paper scissors Game
import random

option = ("rock", "paper", "scissors")
playing = True

while playing:
    player = None
    computer = random.choice(option)
    while player not in option:
        player = input("Enter a choice: rock, paper, scissors? ")

    print(f"player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == 'paper' and computer == 'rock':
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose.")

    if not input("play again? (yes/no): ").lower() == 'yes':
        playing = False

print("Thanks for playing!")


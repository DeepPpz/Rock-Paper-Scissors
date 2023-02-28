import random

rock, paper, scissors = "Rock", "Paper", "Scissors"

player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid input. Try again...")

computer_random = random.randint(1, 3)

computer_move = ""

if computer_random == 1:
    computer_move = rock
elif computer_random == 2:
    computer_move = paper
elif computer_random == 3:
    computer_move = scissors

print(f"The computer chose {computer_move}")

if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    result = "You win!"
elif player_move == computer_move:
    result = "Draw!"
else:
    result = "You lose!"

print(result)
import random
import time

beginning = input("Hello, fella! Want to play a game? [y/n]")

while True:
    if beginning == "n":
        print("Oh, no :(. Well, goodbye!")
        exit(0)
    elif beginning == "y":
        print("Alright, let's go! ^_^ ")
        time.sleep(1)
        print("Loading...")
        break
    else:
        print("Woah, I didn't quite catch that.")
        beginning = input("Want to play a game? [y/n]")

rock, paper, scissors = "Rock", "Paper", "Scissors"

time.sleep(3)
player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

if player_move == "r":
    player_move = "Rock"
elif player_move == "p":
    player_move = "Paper"
elif player_move == "s":
    player_move = "Scissors"
else:
    raise SystemExit("Invalid input. Try again...")

print("Now wait for the computer to choose...")
print("1...")
print("2...")
print("3...")

computer_random = random.randint(1, 3)

computer_move = ""

if computer_random == 1:
    computer_move = "Rock"
elif computer_random == 2:
    computer_move = "Paper"
elif computer_random == 3:
    computer_move = "Scissors"

print(f"The computer chose {computer_move}!")

if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    result = "You win!"
elif player_move == computer_move:
    result = "Draw!"
else:
    result = "You lose!"

print(result)
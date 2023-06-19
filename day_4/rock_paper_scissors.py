import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

game_images = [rock, paper, scissors]

print("Rock, paper, scissors game. Choose your destiny.")

your_choice = int(input("Type 0 for rock, 1 for paper or 2 for scissors.\n"))

if your_choice >= 3 or your_choice < 0:
    print("Invalid input. Exiting.")
else:
    print(game_images[your_choice])

    opponent_choice = random.randint(0, 2)
    print("Your opponent chose:")
    print(game_images[opponent_choice])


    if your_choice == 0 and opponent_choice == 2:
        print("You win!")
    elif opponent_choice == 0 and your_choice == 2:
        print("You lose!")
    elif opponent_choice > your_choice:
        print("You lose!")
    elif your_choice > opponent_choice:
        print("You win!")
    elif opponent_choice == your_choice:
        print("Draw.")
    else:
        print("Invalid input. Exiting.")

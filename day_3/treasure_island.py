print("Welcome to Treasure Island")
print("You must find the hidden treasure.")

choice1 = input('You\'re at a crossroad, where do you go? Go "left" or "right": ').lower()

if choice1 == "left":
    choice2 = input("You've come to the lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.: ").lower()
    if choice2 == "wait":
        choice3 = input("You are at the island now. House with 3 doors - Red, yellow, blue. Pick the color of the door to choose:").lower()
        if choice3 == "red":
            print("You got unalived by a pirate.")
        elif choice3 == "yellow":
            print("Found the treasure! You win!")
        elif choice3 == "blue":
            print("You are eaten by a kraken.")
        else:
            print("You are indecisive and chose the wrong answer. You are unalived.")
    else:
        print("You are unalived. Eaten by shark.")
else:
    print("You are unalived. Game Over")
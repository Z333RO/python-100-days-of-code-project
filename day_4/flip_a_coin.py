import random

print("Time to face your fate. Let's flip a coin.")

random_side = random.randint(0, 2)
if random_side == 0:
    print("Heads")
elif random_side == 1:
    print("Tails")
else:
    print("Coin lands on the edge. You now have psychic powers.")

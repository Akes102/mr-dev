# dice_roller.py
import random

history = []

print("Dice roller. Press Enter to roll, type 'q' to quit.")

while True:
    cmd = input("Roll? ").strip().lower()
    if cmd == "q":
        break

    roll = random.randint(1, 6)
    history.append(roll)
    print("You rolled:", roll)
    print("History:", history)

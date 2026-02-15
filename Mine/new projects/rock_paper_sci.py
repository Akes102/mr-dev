# rps.py
import random

choices = ["rock", "paper", "scissors"]

print("Rock Paper Scissors. Type 'q' to quit.")

while True:
    user = input("Pick rock/paper/scissors: ").strip().lower()
    if user == "q":
        break
    if user not in choices:
        print("Invalid choice.")
        continue

    comp = random.choice(choices)
    print("Computer picked:", comp)

    if user == comp:
        print("Draw.")
    elif (user == "rock" and comp == "scissors") or (user == "paper" and comp == "rock") or (user == "scissors" and comp == "paper"):
        print("✅ You win!")
    else:
        print("❌ You lose!")

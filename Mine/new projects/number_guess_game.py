# guess_game.py
import random

secret = random.randint(1, 50)
tries = 0

print("Guess the number (1 to 50). Type 'q' to quit.")

while True:
    user = input("Your guess: ").strip().lower()
    if user == "q":
        print(f"Bye! The number was {secret}.")
        break

    if not user.isdigit():
        print("Enter a number please.")
        continue

    guess = int(user)
    tries += 1

    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")
    else:
        print(f"🎉 Correct! You got it in {tries} tries.")
        break

# atm_sim.py

PIN = "1234"
balance = 500.0

for _ in range(3):
    entered = input("Enter PIN: ").strip()
    if entered == PIN:
        break
else:
    print("Too many wrong PIN attempts.")
    raise SystemExit

while True:
    print("\n1) Balance  2) Deposit  3) Withdraw  4) Quit")
    choice = input("Choose: ").strip()

    if choice == "1":
        print("Balance: R", round(balance, 2))
    elif choice == "2":
        amt = input("Deposit amount: ").strip()
        try:
            amt = float(amt)
            if amt <= 0:
                print("Must be positive.")
            else:
                balance += amt
                print("Deposited.")
        except ValueError:
            print("Invalid amount.")
    elif choice == "3":
        amt = input("Withdraw amount: ").strip()
        try:
            amt = float(amt)
            if amt <= 0:
                print("Must be positive.")
            elif amt > balance:
                print("Not enough funds.")
            else:
                balance -= amt
                print("Withdrawn.")
        except ValueError:
            print("Invalid amount.")
    elif choice == "4":
        print("Bye!")
        break
    else:
        print("Invalid option.")

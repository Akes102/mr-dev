balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Amount must be positive")

    if amount > balance:
        raise ValueError("Insufficient balance")

    balance -= amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)

except ValueError as e:
    print("Error:", e)

finally:
    print("Thank you for using ATM")



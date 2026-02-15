# calculator.py

def calc(a, op, b):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    return "Unknown operator"

print("Calculator: +  -  *  /   (type 'q' to quit)")

while True:
    a = input("First number: ").strip().lower()
    if a == "q":
        break
    op = input("Operator: ").strip()
    b = input("Second number: ").strip()

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("Numbers only.")
        continue

    print("Result:", calc(a, op, b))

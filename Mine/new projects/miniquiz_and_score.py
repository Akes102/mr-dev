# quiz_game.py

questions = [
    ("What does CPU stand for?", "central processing unit"),
    ("What keyword creates a function in Python?", "def"),
    ("What data type is [1,2,3]?", "list"),
    ("What does len() do?", "returns length"),
]

score = 0

for q, ans in questions:
    user = input(q + " ").strip().lower()
    if user == ans:
        print("✅ Correct")
        score += 1
    else:
        print("❌ Wrong. Answer:", ans)

print(f"Final score: {score}/{len(questions)}")

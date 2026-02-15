# grade_tracker.py

grades = []

print("Enter grades (0-100). Type 'done' to finish.")

while True:
    g = input("Grade: ").strip().lower()
    if g == "done":
        break
    if not g.isdigit():
        print("Numbers only.")
        continue

    num = int(g)
    if 0 <= num <= 100:
        grades.append(num)
    else:
        print("Grade must be 0 to 100.")

if not grades:
    print("No grades entered.")
else:
    avg = sum(grades) / len(grades)
    print("Grades:", grades)
    print("Average:", round(avg, 2))
    print("Result:", "PASS ✅" if avg >= 50 else "FAIL ❌")

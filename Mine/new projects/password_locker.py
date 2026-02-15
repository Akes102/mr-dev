# password_locker.py

CORRECT_PASSWORD = "python123"
MAX_TRIES = 3

for attempt in range(1, MAX_TRIES + 1):
    entered = input(f"Attempt {attempt}/{MAX_TRIES} - Enter password: ").strip()

    if entered == CORRECT_PASSWORD:
        print("✅ Access granted!")
        break
    else:
        print("❌ Incorrect password.")

if entered != CORRECT_PASSWORD:
    print("🚫 Too many attempts. Locked out.")

password = "Code123"

if len(password) < 4:
    print("too short")
elif password.isalpha():
    print("weak")
elif password.isalnum():
    print("medium")
else:
    print("strong")


#opening a file

file =open("data.txt","r")
print(file.read())
file.close()

#open with try-except

try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found")

finally:
    try:
        file.close()
    except NameError:
        pass



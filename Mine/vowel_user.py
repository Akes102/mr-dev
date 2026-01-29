
'''the user must input data then replace the vowels in that data with * and print the result'''

def user_vowels(str):
    vowels="aeiou"
    result=""
    
    for char in str:
        if char.lower() in vowels:
            result += "*"
        else:
            result+=char
    return result

sentence = input("Enter a sentence: ")
output = user_vowels(sentence)
print(output)   
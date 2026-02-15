# vowel_counter.py

def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count

sentence = input("Enter a sentence: ")
print("Vowel count:", count_vowels(sentence))

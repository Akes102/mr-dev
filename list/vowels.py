 
#write a function to change the vowels into *   
 
def bleep_vowels(str):
    new_str =""
    vowels ="aeiou"
    
    #write a loop to iterate through the characters
    
    for char in str:
    
        #write a statement to capture vowels and replace it
        
        if char in vowels:
            new_str += "*"
        else:
            new_str += char
       
    return new_str
    
#call the function to iterate through the characters 
#and replace it with * 
   
print(bleep_vowels("skateboard"))
print(bleep_vowels("slipper"))
print(bleep_vowels("range"))
print(bleep_vowels("brisk morning"))
'''
print("I am the python God")

age=10

print(age)

name = input("what is your name? ")
print("hello ",name)

color = input("What is your favourite color? ")
print("my favourite color is: ",color)


#using if statements(u basicaly saying if this 
# true then do this otherwise do that)
age = int(input("what is your age? "))

if age >= 18:
    print("You may enter")
else:
    print("you are to young!")


#testing myself to creat a password checker
#using if statement

password =(input("please enter password!"))
if password == "python123":
    print("Access granted!")
else:
    print("incorrect password!! try again!")
    

name=input("what is the name of your boss? ")

if name == "Troy":
    print("weldone thats correct!")
else:
    print("Sorry, you are wrong!")
 
 
#loops...basically the computer saying 
#ill do this over and over util you say stop

#this will print hello 5 times
for i in range(5):
    print("hello")

#adding a start, stop and step to the loop

for j in range(1, 11, 2):
    print(j)
print("Blast off!!!")

#lets create a timer counting down

for t in range(10, 0, -1):
    print(t)
print("Happy new year")



#lists, tuples, sets
#list are like a backpack but its changeable
#tuples are like a locked box
#sets are messy piles but has no dups

#ask the user for 3 favourite fruits
fruits=[]

for i in range(3): #looping 3 times to ask 3 fruits
    fruit=input("Enter a fruit. ")
    fruits.append(fruit) #add the answers to this emty list
    print("fruit list: ",fruits)


student_names=[]
for s in range(5):
    names=input("Capture new student")
    student_names.append(names)
    print("New students: ",student_names)


#Dictionaries(name and value pairs)
#it acts like a real dictionary, u look up the word
#and it gives the meaning, in python we search with 
#key and then we get the values associated with the key

student_data={
    "name": "Alex",
    "age": 14,
    "grade": "8"    
}
print(student_data)

my_data={
    "name": "Arnold",
    "age": 31,
    "occupation":"Ai Engineer",
    "hobbies": "coding"
}
print(my_data)



#Functions
#functions is like a machine u build once
#and use it over and over again to do task

#im creating a function that doubles the vowels 
#in a word
def double_vowel(word):
    new_word="" #this is where our new word will be stored
    for i in word:
        if i in "aeiou": #if these leters are the current index
            new_word+=i*2 #then the new word is the current index + that index
        else:
            new_word+=i #if no vowels then just add that index once
    return new_word #return the new word now including the double

print(double_vowel("cat"))
print(double_vowel("runner"))
print(double_vowel("stoplight"))

name="Arnold"
for j in name:
    if j in name == "Arnold":
        name+=" Muller"
        print(name)
'''
#repeat a something 3 times
def repeat(name, times):
    for i in range(times):
        print(name)
repeat("alex",3)

def repeat_year(year, days):
    for j in range(days):
        print(year)
repeat_year("2026", 5)

#coutning up from 0 to 10
def count_up(number):
    for i in range(number + 1):
        print(i)
count_up(10)

#check odd or even
#remember to call integers we use a list[] 
def odd_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num, "is even")
        else:
            print(num, "is odd")
odd_even([1, 65, 8, 20, 7, 6])

def count_vowels(word):
    count=0
    for letter in word:
        if letter in "aeiouAEIOU":
            count+=1
    return count
        
print(count_vowels("Hi my name is Arnold"))



name = input("what is your name? :")

print (name)
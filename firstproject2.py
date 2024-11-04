name = "benjamin karioki"
print(name.capitalize()) #capitalises first letter of only the first word

print(name.title()) #capitalises first letter of each word

print(name.count("a")) #counts number of strings 

print(name.find("b")) # finds the index the letter is in 

print(name.isdigit()) #checks if the string is a digit and ONLY a digit, no other characters

print(name.isalpha()) #checks if the string is alphabetic (only letters no other characters)

print(name.isalnum()) #checks for numbers and letters (no other characters)

print(name.islower()) # all lowercase

print(name.isupper()) #all uppercase

print(name.upper()) # makes all uppercase

print(name.lower()) # makes all lowercase

print(name.replace("e", "3")) #self-explanatory

first = input("first name? ")
family = input("family name? ")
year = input("date of birth? ")

username = first.lower() + family.lower() + year
print("hi", first, "your username is", username)
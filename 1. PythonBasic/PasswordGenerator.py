# Generate a random password
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']

print("Welcome to the PyPassword Generator!")
Letter_numbers = int(input("How many letters would you like in your password? "))

Letter = int(input("How many letters would you like in your password? "))

Symbol_numbers = int(input("How many symbols would you like in your password? "))

numbers = int(input("How many numbers would you like in your password? "))
# Easy level
'''password = ""
for char in range(1, Letter+1):
    password += random.choice(letters)

for sym in range(1, Symbol_numbers+1):
    password += random.choice(symbol)

for number in range(1, numbers+1):
    password += random.choice(numbers1)

print(password)'''
# hard level
password_list = []
for char in range(1, Letter+1):
    password_list.append(random.choice(letters))

for sym in range(1, Symbol_numbers+1):
    password_list.append(random.choice(symbol))

for number in range(1, numbers+1):
    password_list.append(random.choice(numbers1))

random.shuffle(password_list)
print(password_list)

password2 = ""
for char in password_list:
    password2 += char

print(f"Your Password is {password2}")
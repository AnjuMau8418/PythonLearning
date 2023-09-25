'''course="Python For Beginners"
print(course.lower())
print(course.upper())
print(course.title())
print(course.replace('Beginners', 'Absolute Beginners'))
print('python' in course)
# in find method, it uses index, while in in method, it returns boolean values.
print(10**3) # here ** represent the power operator
x=(10+3)*2**2 # paranthesis should be priorities and after thst power operator
import math
print(math.ceil(4.6))# make approximation
print(math.floor(4.6))# print integer value
print(math.factorial(10))
# if statements
is_hot=True
is_cold=False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("wear warm cloths")
else:
    print("it's a lovely day")
print("Enjoy your day")
# Exercise
price=1000000
Good_credit=True
if Good_credit:
    payment= 0.1*price
else:
    payment= 0.2*price
print(f"Payment: ${payment}")
has_good_credit=True
criminal_record=False
if has_good_credit and not criminal_record :
    print("Eligibel for loan")

# Comparison operator
temperature=35
if temperature > 30:
    print("it is a hot day")
else:
    print("it is not a hot day")
# Exercise
name="Aswasthama"
if len(name)< 3:
    print("Name must be atleast three character")
elif len(name) > 50:
    print("Name must be a maximum of 50 character")
else:
    print("Name looks good!")
# Weight conversion
weight=int(input("Enter Weight: "))
unit=input('(L)bs or (K)g :')
if unit.upper()=="L":
     converter=weight * 0.454
else:
    converter=weight/0.454
print(converter)
# while loop Excercise
number=int(input("Enter gussing number: "))
guess_count=0
guess_limit=3
while guess_count < guess_limit:
    Guess=int(input("Guess the number: "))
    guess_count = guess_count + 1
    if number == Guess:
        print("You won!")
        break
else:
    print("Sorry You failed")

info=" "
started=False
helped=True
while True:
    info=input("> ").lower()
    if info == 'help':
            print('start - to start the car, stop - to stop the car, quit - to exit ')'''
''' elif info == 'start':
        if started:
            print("Car already started")
        else:
            started=True
            print("Car started...ready to go!")
    elif info =='stop':
         if not started:
             print("Car is stopped already")
         else:
             started=False
             print("Car stopped..")
    elif info =='quit':
        break
        
    else:
        print("Sorry ! I don't understand that....")
#for loop
for item in range(5,10,2):
    print(item)
# Program to calculate the total cost of all the item in a shoppping cart.
prices=[10,20,30]
total=0
for price in prices:
    total+=price
print(f"Total: { total}")
# Nested loops
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

number = [2, 2, 2, 2, 8]
for x_count in number:
    output = ''
    for count in range(x_count):
        output = output + 'x'
    print(output)
#In list check the largest number
names=[11,4,7,9,5,1]
max=names[0]
for x in names:
  if x > max:
      max= x
print(max)
# 2-Dimentional list
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    for item in row:
        print(item)
# List method
numbers=[5,2,1,5,7,4]
numbers.pop()#remove last item
# clear remove all items from the list, insert used to insert new elements to list,remove is used to remove the elements from the list
print(numbers)
print( 7 in numbers)
print(numbers.count(5))# count how many times number ocur in list
numbers.sort()# sort the list
numbers.reverse()# reverse the list
print(numbers)
# remove duplicates from a list
numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
#unpacking
coordiantes = (1,2,3)
x = coordiantes[0]
y = coordiantes[1]
z = coordiantes[2]
x, y, z = coordiantes # same as above three lines
print(x)
print(y)
print(z)
# Dictionaries
customer= {
    "name": "John smith",
    "age":30,
    "is varified": True
}
customer["name"] = "Jack smith"
customer["birthdate"]= "Jan 1 1980"
print(customer)
# excercise
phone=input("Enter the phone number : ")
digits_mapping = {
    "0":"Zero",
    "1":"one",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)
#Emoji converter
message = input(">")
words= message.split(' ')
emojis = {
    ":)":"Smile Face",
    "(:": "Sad Face",
}
output=""
for word in words:
    output += emojis.get(word,word) + " "
print(output)
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print("Welcomr aboard")
print("Start")
greet_user(last_name="Smith",first_name="John")#use of keyword argument, keyword argument always come after positional argument
print("Finish")
# problem using functions
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "Smile Face",
        "(:": "Sad Face",
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))
#exception handling
try:
   age=int(input("Age: "))
   income=20000
   risk =income /age
   print(age)
except ZeroDivisionError:
    print("Age can't be zero")
except ValueError:
    print("invalid value")
#Classes
class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point1 = Point()
point1.x=10
point1.y=20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 30
print(point2.x)
#constructor-> A function that get called at the time of creating an object

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move(self):
        print("move")
    def draw(self):
        print("draw")

point = Point(10,20)
point.x=11
print(point.x)
# Excercise
class Person:
    def __init__(self, name):
        self.name=name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()
# Inheritance
class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def beannoying(self):
        print("annoying")

cat1= Cat()
cat1.beannoying()
# Modules
import converters
from converters import kg_to_lbs

kg_to_lbs(100)
print(converters.kg_to_lbs(70))
# Excercise
from utils import find_max
numbers = [10, 3, 6, 2]
maximum=find_max(numbers)
print(maximum)'''
# Packages-> A container for multiple modules
from ecommerce.shipping import calc_shipping

calc_shipping()


































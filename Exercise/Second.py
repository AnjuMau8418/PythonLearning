# Generating random number
'''import random

for i in range(3):
    print(random.randint(10,20))

members= ['John','Mary','Bob','Mosh']
Leaders = random.choice(members)
print(Leaders)
# Excercise

import random


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second

dice = Dice()
print(dice.roll())'''
# File and Dictionaries
from pathlib import Path

path = Path()
# print(path.mkdir())-> make directiory
# print(path.rmdir())->remove directiory
for file in path.glob('*'):  # tell about all the files present in directiory
    print(file)

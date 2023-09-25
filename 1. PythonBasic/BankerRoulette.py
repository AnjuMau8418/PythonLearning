# who will pay the bill
import random

test_seed = int(input("Create a seed number:"))
random.seed(test_seed)

NameAsCSV = input("Give me everybody's names, separated by a comma ")
names = NameAsCSV.split(",")
print(names)

# names_generation = random.randint(0, len(names)-1)
# name = names[names_generation]
name = random.choice(names) # by using choice function
print(f"{name} is going to pay the bill.")

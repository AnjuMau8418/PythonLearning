# Head or tail predictor
import random
'''The seed() method is used to initialize the random number generator. The random number generator needs a number to 
start with (a seed value), to be able to generate a random number.'''
test_seed = int(input("Create a seed number:"))
random.seed(test_seed)

random_side = random.randint(0,1)

if random_side == 1:
    print("Heads")
else:
    print("Tails")

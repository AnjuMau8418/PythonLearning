# print("Hello " + input("What is your name? ")+"!")
# print(len(input('What is your name:'))) using len() function
# Random number generator
# import random

"""random.seed(123)
random_integer = random.randint(1, 20)  # integer generator
print(random_integer)

random_float = random.random()  # Floating point generator
print(random_float)
random_float1 = random.uniform(1, 7)
print(random_float1)

# Nesting of Dictionary in a Dictionary
travel_log = {"France": {"visited_cities": ["Paris", "Lille", "Dijon"], "total_visits": 12},
              "Germany": {"visited_cities": ["Berlin", "Hamburg", "Stuttgart"], "total_visited": 15}
              }

# Nesting of Dictionary in a List
travel_log = [
    {"country": "France",
     "visited_cities": ["Paris", "Lille", "Dijon"],
     "total_visit": 12},
    {"Country": "Germany",
     "visited_cities": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visited": 15},
]


# comment key for a line of group: Ctrl+/
# Use of title case
def formate_name(f_name, l_name):
    '''Take a first and last name and format it to return the title case version of the name.'''


# if f_name == "" or l_name == "":
#     return "You didn't provide valid input."
# formated_f_name = f_name.title()
# formated_l_name = l_name.title()
# return f"Result: {formated_f_name} {formated_l_name}"


print(formate_name(input("What is your first name?"), input("What is your last name?")))"""

# Scope
# There is no block scope in python.

import random

'''dice_image = ["😍", "😎", "😱", "😂", "😢", "😥", "🤩"]
dice_num = randint(0, 6)
print(dice_image[dice_num])'''


def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

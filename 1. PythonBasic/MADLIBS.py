# string concatenation
# Suppose we want to creat a string that say "subscribe to __"
# youtuber = "Anju Maurya" # some string variable

# a few ways to do this
# print("Subscribe to " + youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")
adj = input("Adjectives: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")
madlib = f"Computer Programming is so {adj}! It makes me so excited all the times because I love to {verb1}. \
Stay hyderated and {verb2} like you are {famous_person}!"

print(madlib)

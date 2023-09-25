# Treasure Island
print("welcome! to the treasure island!!")
print("Your mission is to find the treasure.")

Direction_to_go = input("You are at a cross road. where do you want to go? 'Left' or 'Right' ?").lower()

if Direction_to_go == "left":
    Choice1 = input("you come to a Lake. There is an Island at the middle of Lake.\nType 'wait' to wait for a boat. "
                    "Type 'swim' to swim across. ").lower()
    if Choice1 == "wait":
        Choice2 = input("you arrive at the island unharmed.There is a house with three doors. one red, one blue and "
                        "one yellow.\nWhich colour would you choose?").lower()
        if Choice2 == "blue":
            print("You enter a room of beast. Game Over!")
        elif Choice2 == "yellow":
            print("You found the treasure. You Win!")
        elif Choice2 == "red":
            print("It is room with full of fires. Game over")
        else:
            print("You choose a room that does not exist. Game Over!")
    else:
        print("You got attacked by an angry trout. Game Over!")
else:
    print("You fall into a hole.Game Over!")

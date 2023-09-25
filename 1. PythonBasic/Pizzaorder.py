# Pizza order
print("Welcome! to Python Pizza Deliveries!")
Price_smallPizza = 15
Price_mediumPizza = 20
Price_largePizza = 25
Price_of_pepperoni_for_smallPizza = 2
Price_of_pepperoni_for_medium0r_largePizza = 3
Price_for_cheese_for_any_sizePizza = 1
size = input("Which size Pizza do you want? S, M or L? ")
add_pepperoni = input("Do you want pepperoni? Yes or No? ")
extra_cheese = input("Do you want extra cheese ? Yes or No ?")
if size == "S":
    if add_pepperoni == "Yes":
        total_price = Price_smallPizza + Price_of_pepperoni_for_smallPizza
        print(f"You have to pay {total_price}$ for you Pizza Order.")
    if extra_cheese == "Yes":
        total_price = Price_smallPizza + Price_for_cheese_for_any_sizePizza
        print(f"You have to pay {total_price}$ for you Pizza Order.")
    if add_pepperoni == "Yes" and extra_cheese == "Yes":
        total_price = Price_smallPizza + Price_of_pepperoni_for_smallPizza + Price_for_cheese_for_any_sizePizza
        print(f"You have to pay {total_price}$ for you Pizza Order.")


if size == "M":
    if add_pepperoni == "Yes":
        total_Price = Price_of_pepperoni_for_medium0r_largePizza + Price_mediumPizza
        print(f"you have to pay {total_Price} $ for you Pizza Order.")
    if extra_cheese == "Yes":
        total_Price = Price_mediumPizza + Price_for_cheese_for_any_sizePizza
        print(f"you have to pay {total_Price} $ for you Pizza Order.")
    if add_pepperoni == "Yes" and extra_cheese == "Yes":
        total_Price = Price_mediumPizza + Price_of_pepperoni_for_medium0r_largePizza+Price_for_cheese_for_any_sizePizza
        print(f"you have to pay {total_Price} $ for you Pizza Order.")

if size == "L":
    if add_pepperoni == "Yes":
        total_Price = Price_of_pepperoni_for_medium0r_largePizza + Price_largePizza
        print(f"you have to pay {total_Price} $ for you Pizza Order.")
    if extra_cheese == "Yes":
        total_Price = Price_largePizza + Price_for_cheese_for_any_sizePizza
        print(f"you have to pay {total_Price} $ for you Pizza Order.")
    if add_pepperoni == "Yes" and extra_cheese == "Yes":
        total_Price = Price_largePizza + Price_of_pepperoni_for_medium0r_largePizza + Price_for_cheese_for_any_sizePizza
        print(f"you have to pay {total_Price} $ for you Pizza Order.")

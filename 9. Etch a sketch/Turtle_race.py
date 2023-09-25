from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)  # setup screen size
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle would win the race? Enter the color : ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
y = -100
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    y = y + 30
    x = -230
    new_turtle.goto(x, y)
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle is winner.")
            else:
                print(f"You've lost. The {winning_color} turtle is winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

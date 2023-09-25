# from turtle import Turtle, Screen
# from turtle import * -> it imports all associated classes or files of that package
# timmy_the_turtle = Turtle()
# screen = Screen()
# screen.exitonclick()
# Generate random walk with random color
import turtle as t
import random

tim = t.Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed('fastest')
for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))


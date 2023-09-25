'''import colorgram

rgb_colors = []
colors = colorgram.extract('hirst.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)'''
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(235, 241, 238), (194, 160, 121), (73, 92, 124), (142, 87, 59), (216, 209, 122), (140, 160, 187),
              (183, 147, 162), (29, 33, 46), (56, 35, 26), (174, 160, 42), (121, 73, 92), (141, 174, 154),
              (79, 115, 80), (60, 30, 39), (137, 27, 18), (117, 30, 43), (184, 100, 86), (47, 59, 92), (101, 119, 168),
              (174, 100, 116), (34, 51, 45), (103, 155, 89), (214, 176, 191), (217, 180, 173), (165, 208, 187),
              (66, 83, 27), (179, 186, 212)]
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    tim.dot(15, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()

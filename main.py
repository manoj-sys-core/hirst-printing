import random
import turtle
from turtle import Turtle,Screen
turtle.colormode(255)
tim = Turtle()
tim.speed("fast")
tim.penup()
tim.hideturtle()

color_list = [(226, 231, 237), (227, 236, 234), (58, 106, 147), (235, 227, 209), (224, 201, 112), (132, 86, 60), (220, 140, 70), (195, 145, 170), (139, 176, 201), (238, 225, 234), (138, 80, 104), (189, 82, 112), (211, 93, 66), (67, 108, 92), (133, 181, 136), (130, 135, 77), (63, 156, 96), (47, 156, 190), (184, 192, 202), (216, 175, 188), (17, 58, 92), (23, 67, 111), (113, 123, 150), (126, 39, 49), (231, 175, 162), (156, 207, 216), (171, 205, 184), (68, 56, 42), (78, 64, 46), (46, 76, 69)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_dots = 101
for dot in range(1, num_dots):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
dis = Screen()
dis.exitonclick()
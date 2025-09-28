from turtle import Turtle, Screen
import random

tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side in range(3, 11):
    tim.color(random.choice(colours))
    draw_shapes(shape_side)

screen = Screen()
screen.exitonclick()
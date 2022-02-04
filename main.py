import colorgram,random

# hirst_colors = colorgram.extract('hirst_data.jpeg', 30)
# # print(hirst_color[0].rgb)
# rgb_colors = []
# for color in hirst_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
#
#Already retreive the rgb data from a hirst paiting jpeg file.
color_list = [(237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177), (216, 134, 179), (8, 186, 216), (229, 167, 200), (210, 25, 148), (122, 190, 160), (7, 49, 26), (34, 136, 72), (63, 20, 7), (126, 219, 234), (190, 14, 4), (109, 87, 215), (140, 217, 202), (238, 64, 34), (71, 10, 28)]

#Start to create a hirsting painting nominating script
from turtle import Screen,Turtle
import turtle as tt

turtle = Turtle()
tt.colormode(255)
turtle.speed("fastest")
turtle.hideturtle()
turtle.up()


turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

num_dots = 100

for num_count in range(1, num_dots+1):
    turtle.dot(23, random.choice(color_list) )
    turtle.forward(50)
    if num_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)
screen = Screen()
screen.exitonclick()
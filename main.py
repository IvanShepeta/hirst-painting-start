# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.b
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
# we take the color from images
import random
import turtle as t
t.colormode(255)
color_list = [(202, 110, 110), (149, 50, 50), (222, 136, 136), (53, 123, 123), (170, 41, 41), (138, 20, 20), (134, 184, 184), (197, 73, 73), (47, 86, 86), (73, 35, 35), (145, 149, 149), (14, 70, 70), (232, 165, 165), (160, 158, 158), (54, 50, 50), (101, 77, 77), (183, 171, 171), (36, 74, 74), (19, 89, 89), (82, 129, 129), (147, 19, 19), (27, 102, 102), (12, 64, 64), (107, 153, 153), (176, 208, 208), (168, 102, 102)]
tim = t.Turtle()
tim.speed("fastest")
tim.penup()

def draw_line(time):
    x = -250
    y = -250
    for o in range(0, time):
        tim.teleport(x, y)
        for i in range(0, 10):
            tim.dot(20,random.choice(color_list))
            tim.forward(50)
            y += 5
draw_line(10)
screen = t.Screen()

screen.exitonclick()

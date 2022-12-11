from turtle import *

title("turtle tree")

speed('fastest')

right(-90)
angle = 30

def tree (size, level):
    if level > 0:
        colormode(255)
        pencolor(0, 255//level, 0)

        forward(size)
        right(angle)

        tree(0.8 * size, level - 1)
        pencolor(0, 255//level, 0)
        left(2 * angle)

        tree(0.8 * size, level - 1)
        pencolor(0, 255//level, 0)

        right(angle)
        forward(-size)

tree(60, 10)

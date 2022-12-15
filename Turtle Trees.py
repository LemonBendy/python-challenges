# Recursive Tree Challenge - www.101computing.net/recursive-tree-challenge
from turtle import *


# Recursive function to draw a tree, branch by branch
def drawtree(level, size, angle, ratio):
    if level >= 0:
        forward(size)
        left(angle)
        drawtree(level - 1, size / ratio, angle, ratio)
        right(2 * angle)
        # Draw right branch of the tree
        drawtree(level - 1, size / ratio, angle, ratio)
        left(angle)
        forward(-size)
    else:
        # Stop the recursion
        return


# Main Program Starts Here
speed(0)
penup()
goto(0, -180)
left(90)
pendown()

# Draw a tree using a recursive function
size = 90
angle = 90
ratio = 1
level = 360

drawtree(level, size, angle, ratio)

import turtle
import math
import random


def square(side_length, initial_rotation=0):
    turtle.left(initial_rotation)
    for i in range(0, 4):
        turtle.forward(side_length)
        turtle.left(90)


def triangle(side_length):
    for i in range(0, 3):
        turtle.forward(side_length)
        turtle.left(120)


def pentagon(side_length):
    for i in range(0, 5):
        turtle.forward(side_length)
        turtle.left(72)


def polygon(side_length, num_sides, user_color='black'):
    turtle.color(user_color)
    x = random.randrange(-100, 100)
    y = random.randrange(-100, 100)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(0, num_sides):
        turtle.forward(side_length)
        turtle.left(360 / num_sides)


def circle(radius):
    NUM_SIDES = 100
    side_length = 2 * math.pi * radius / NUM_SIDES
    polygon(side_length, NUM_SIDES)


def draw_spiral(line_len):
    if line_len < 10:
        return
    turtle.forward(line_len)
    turtle.left(270)
    turtle.forward(line_len)
    turtle.left(270)
    line_len -= line_len / 10
    draw_spiral(line_len)


def recursive_polygon(side_length, num_sides, step):
    if step < 1:
        return
    turtle.forward(side_length)
    turtle.left(180 - (num_sides - 2) * 180 / num_sides)
    recursive_polygon(side_length, num_sides, step - 1)


def spiral_square(side):
    if side < 10:
        return
    turtle.forward(side)
    turtle.left(72)
    turtle.forward(side)
    turtle.left(72)
    spiral_square(side - 10)


def concentric_circle(radius):
    if radius > 500:
        return
    turtle.penup()
    turtle.right(90)
    turtle.forward(radius)
    turtle.right(270)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.home()
    concentric_circle(radius + 10)


if __name__ == "__main__":

    print("Turtle Fun!")

    side_length = int(input(f"I am going to draw a square. How long would like "
                            f"the side length to be?"))
    initial_rotation = int(input("What would you like the initial rotation "
                                 "to be?"))
    square(side_length, initial_rotation)
    triangle(side_length)
    pentagon(side_length)
    polygon(side_length, 3)

    circle(100)
    square(100)
    turtle.exitonclick()

    type_of_shape = input(
        "What type of shape would you like to draw? (triangle, square, "
        "pentagon, sextagon, septagon, octagon, nonagon, decagon, dodecagon, "
        "circle) ")
    side_length = int(input("How long should each side be? "))
    sides = {'triangle': 3, 'square': 4, 'pentagon': 5, 'sextagon': 6,
             'septagon': 7, 'octagon': 8, 'nonagon': 9, 'decagon': 10,
             'dodecagon': 12}
    if type_of_shape == 'circle':
        circle(side_length)
    else:
        polygon(side_length, sides.get(type_of_shape))

    draw_spiral(100)
    recursive_polygon(100, 6, 6)

    color = str(input("what color do you want?"))
    polygon(100, 5, color)

    shape = int(input("What type of shape would you like to draw?"))
    polygon(100, shape)

    spiral_square(200)

    concentric_circle(50)

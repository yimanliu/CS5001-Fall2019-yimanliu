import turtle
import random
import time


def draw_something(some_turtle):
    some_turtle.forward(100)
    some_turtle.right(144)


def draw_by(name):
    name.shape(random.choice(SHAPES))
    name.pencolor(random.choice(COLORS))
    name.penup()
    name.goto(random.randint(-WIDTH, WIDTH),
              random.randint(-HEIGHT, HEIGHT))


if __name__ == '__main__':
    mywindow = turtle.Screen()
    SHAPES = ['turtle', 'circle', 'arrow',
              'square', 'triangle', 'classic']
    COLORS = ['red', 'blue', 'green',
              'black', 'orange', 'purple']
    WIDTH = 400
    HEIGHT = 300
    suzy = turtle.Turtle()
    draw_by(suzy)

    mark = turtle.Turtle()
    draw_by(mark)

    marie = turtle.Turtle()
    draw_by(marie)

    jose = turtle.Turtle()
    draw_by(jose)

    becky = turtle.Turtle()
    draw_by(becky)

    for i in range(5):
        for mytur in [suzy, mark, jose, marie, becky]:
            mytur.pendown()
            mytur.showturtle()
            draw_something(mytur)
            mytur.hideturtle()
            time.sleep(0.5)

    mywindow.exitonclick()

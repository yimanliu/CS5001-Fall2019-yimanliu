from tkinter import Tk, Canvas, Frame, BOTH
import random
import math
import time

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
WINDOW_TOP_X = 300
WINDOW_TOP_Y = 300


class Ball:
    """
    The Ball class defines a "ball" that can bounce around the screen
    """

    def __init__(self, canvas, x=-1, y=-1, random_loc=False, shape='rectangle'):
        self.canvas = canvas
        self.shape = shape
        if random_loc:
            self.x = random.randint(0, canvas.winfo_width() - 1)
            self.y = random.randint(0, canvas.winfo_height() - 1)
        else:
            if x == -1:
                self.x = canvas.winfo_width() / 2
            else:
                self.x = x
            if y == -1:
                self.y = canvas.winfo_height() / 2
            else:
                self.y = y
        self.width = random.randint(0, 30)
        self.height = random.randint(0, 30)
        self.direction = random.randint(0, 359) / (2 * math.pi)
        self.fill = "#" + ("%06x" % random.randint(0, 16777215))
        self.outline = self.fill
        self.draw()

    def draw(self):
        if self.shape == 'rectangle':
            self.canvas_object = self.canvas.create_rectangle(self.x, self.y,
                                                              self.x +
                                                              self.width,
                                                              self.y + self.height,
                                                              outline=self.outline,
                                                              fill=self.fill)

    def update(self):
        x_dir = math.cos(self.direction)
        y_dir = math.sin(self.direction)

        self.x += x_dir * 10
        self.y += y_dir * 10

        if self.x < 0:
            self.x = 0
            x_dir *= -1

        if self.x > self.canvas.winfo_width():
            self.x = self.canvas.winfo_width()
            x_dir *= -1

        if self.y < 0:
            self.y = 0
            y_dir *= -1

        if self.y > self.canvas.winfo_height():
            self.y = self.canvas.winfo_height()
            y_dir *= -1

        self.direction = math.atan2(y_dir, x_dir)
        self.canvas.delete(self.canvas_object)
        self.draw()


class Playground(Frame):
    """
    The Playground class is the part of the screen where we can draw things
    """

    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self)
        self.initUI()

    def initUI(self):
        """
        The UI Initialization function.
        :return: None
        """
        self.master.title("Bouncing Balls")
        self.pack(fill=BOTH, expand=1)
        self.canvas.pack(fill=BOTH, expand=1)

    def get_canvas(self):
        return self.canvas


def animate(playground):
    canvas = playground.get_canvas()

    ball_list = [Ball(canvas, random_loc=True) for b in range(360)]
    while True:
        for ball in ball_list:
            ball.update()
        canvas.update()


def main():
    root = Tk()
    root.geometry(str(CANVAS_WIDTH) + "x" +
                  str(CANVAS_HEIGHT) + "+" +
                  str(WINDOW_TOP_X) + "+" +
                  str(WINDOW_TOP_Y))

    playground = Playground()

    root.after(1000, lambda: animate(playground))
    root.mainloop()


if __name__ == "__main__":
    main()

from tkinter import Tk, Canvas, BOTH, LEFT, RIGHT, TOP, RAISED, NONE
from tkinter import Frame, Button
import tkinter as tk

import random
import queue

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
WINDOW_TOP_X = 300
WINDOW_TOP_Y = 300
FALL_RATE = 0  # the higher, the slower it falls
PART_SIZE = 10


class Particle:
    """
    The Particle class defines a "particle" that is affected by gravity
    """
    grid = []  # will be set by the playground

    def __init__(self, canvas, row, col, fill='white'):
        """
        Initializes the Particle instance
        :param canvas: a canvas to draw onto
        :param row: the starting row
        :param col: the starting column
        :param fill: the particle color
        """
        self.canvas = canvas
        self.last_drawn = None
        self.col = col
        self.row = row
        self.width = PART_SIZE
        self.height = PART_SIZE
        self.fill = fill
        self.outline = self.fill
        self.draw()

    def draw(self):
        if self.last_drawn is not None:
            self.canvas.delete(self.last_drawn)
        self.last_drawn = (
            self.canvas.create_rectangle(self.col * PART_SIZE,
                                         self.row * PART_SIZE,
                                         self.col * PART_SIZE +
                                         self.width,
                                         self.row * PART_SIZE + self.height,
                                         outline=self.outline,
                                         fill=self.fill))

    def calculate_movement(self, row_offset, col_offset):
        row = self.row + row_offset
        col = self.col + col_offset
        if row > len(Particle.grid) - 1:
            row = len(Particle.grid) - 1
        if col > len(Particle.grid[0]) - 1:
            col = len(Particle.grid[0]) - 1
        if col < 0:
            col = 0
        return row, col

    def update(self):
        new_row, new_col = self.calculate_movement(1, 0)  # default is to
        # move one down
        if not (new_col == self.col and new_row == self.row):
            old_particle = Particle.grid[new_row][new_col]
            Particle.grid[self.row][self.col] = old_particle
            if old_particle is not None:
                old_particle.row = self.row
                old_particle.col = self.col
                old_particle.draw()
            self.col = new_col
            self.row = new_row
            Particle.grid[new_row][new_col] = self
            self.draw()
        return self.row, self.col


class Metal(Particle):
    """
    Metal does not move.
    """

    # TODO: Your code here
    def __init__(self, canvas, row, col, fill='gray40'):
        self.canvas = canvas
        self.last_drawn = None
        self.row = row
        self.col = col
        self.width = PART_SIZE
        self.height = PART_SIZE
        self.fill = fill
        self.outline = self.fill
        self.draw()

    def update(self):
        if Particle.grid[self.row][self.col] is None:
            Particle.grid[self.row][self.col] = self
            self.draw()
        return self.row, self.col


class Sand(Particle):
    """
    Sand works like this: before moving, check the position below it. If the
    position is empty, it can move. Otherwise, it has to stay put.
    """

    # TODO: Your code here
    def __init__(self, canvas, row, col, fill='dark khaki'):
        self.canvas = canvas
        self.last_drawn = None
        self.row = row
        self.col = col
        self.width = PART_SIZE
        self.height = PART_SIZE
        self.fill = fill
        self.outline = self.fill
        self.draw()

    def update(self):
        new_row, new_col = self.calculate_movement(1, 0)
        if new_col == self.col and new_row == self.row:
            return self.row, self.col
        old_particle = Particle.grid[new_row][new_col]
        if old_particle is None:
            Particle.grid[self.row][self.col] = None
        elif old_particle is not None:
            if isinstance(old_particle, Water):
                Particle.grid[self.row][self.col] = old_particle
                old_particle.row = self.row
                old_particle.col = self.col
                old_particle.draw()
            else:
                return self.row, self.col
        self.col = new_col
        self.row = new_row
        Particle.grid[new_row][new_col] = self
        self.draw()
        return self.row, self.col


class Water(Particle):
    """
    Water works like this: if there is nothing below it, simply fall.
    If there is something below it, randomly choose a sideways direction,
    left or right. If there is nothing in that direction, then the
    water should move to that spot.
    """

    # TODO: Your Code Here
    def __init__(self, canvas, row, col, fill='blue'):
        self.canvas = canvas
        self.last_drawn = None
        self.row = row
        self.col = col
        self.width = PART_SIZE
        self.height = PART_SIZE
        self.fill = fill
        self.outline = self.fill
        self.draw()

    def update(self):
        new_row, new_col = self.calculate_movement(1, 0)
        if new_col == self.col and new_row == self.row:
            return self.row, self.col
        if Particle.grid[new_row][new_col] is not None:
            new_row = self.row
            new_col += random.randint(-1, 1)
        old_particle = Particle.grid[new_row][new_col]
        if old_particle is None:
            Particle.grid[self.row][self.col] = None
            self.col = new_col
            self.row = new_row
            Particle.grid[new_row][new_col] = self
            self.draw()
        return self.row, self.col


class Playground(Frame):
    """
    The Playground class is the part of the screen where we can draw things
    """

    def __init__(self):
        super().__init__()
        self.canvas = None  # will define in initUI
        self.particles_strings = ['Metal', 'Sand', 'Water']
        self.particle_classes = [Metal, Sand, Water]
        self.v = tk.IntVar()
        self.v.set(0)  # default is Metal
        self.init_ui()
        self.grid_locs = set()
        self.grid = [[None] * (CANVAS_WIDTH // PART_SIZE)
                     for col in range(CANVAS_HEIGHT // PART_SIZE)]
        self.num_particles = 0
        self.queue = queue.Queue()  # for adding new particles with the mouse
        self.need_to_clear = False

    def init_ui(self):
        """
        The UI Initialization function.
        :return: None
        """

        self.master.title("Falling Particles")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.canvas = Canvas(frame, bg='black')
        self.canvas.pack(fill=BOTH, expand=True)

        self.pack(fill=BOTH, expand=True)

        for i, p in enumerate(self.particles_strings):
            tk.Radiobutton(self,
                           text=p,
                           padx=20,
                           variable=self.v,
                           value=i).pack(anchor=tk.W)

        button = Button(self,
                        text="Clear",
                        command=self.clear).pack(anchor=tk.W)

        button = Button(self,
                        text="Quit",
                        command=quit).pack(anchor=tk.W)

    def clear(self):
        self.need_to_clear = True

    def clear_particles(self):
        print("Clearing particles")
        for row, col in self.grid_locs:
            particle = self.grid[row][col]
            particle.canvas.delete(particle.last_drawn)

        self.grid = [[None] * (CANVAS_WIDTH // PART_SIZE)
                     for col in range(CANVAS_HEIGHT // PART_SIZE)]
        Particle.grid = self.grid
        self.grid_locs = set()
        self.need_to_clear = False

    def mouse_moved(self, event):
        canvas = self.get_canvas()
        if (event.x < 0 or event.y < 0 or event.x >= canvas.winfo_width() or
                event.y > canvas.winfo_height()):
            return
        col, row = event.x // PART_SIZE, event.y // PART_SIZE
        try:
            if canvas.mouse_down:
                particle_class = self.particle_classes[self.v.get()]
                self.queue.put((particle_class, row, col))
        except AttributeError:
            pass

        canvas.old_coords = col, row

    def mouse_button(self, event, button_down):
        try:
            if event.widget._name != '!canvas':
                return  # we didn't click on the canvas
        except AttributeError:  # no _name
            return

        canvas = self.get_canvas()
        canvas.mouse_down = button_down
        # print(event.x, event.y)
        if button_down:
            col, row = event.x // PART_SIZE, event.y // PART_SIZE
            particle_class = self.particle_classes[self.v.get()]
            self.queue.put((particle_class, row, col))

    def get_canvas(self):
        return self.canvas

    def get_new_particles(self):
        while not self.queue.empty():
            particle_class, row, col = self.queue.get()
            if self.grid[row][col] is None:
                self.grid[row][col] = particle_class(self.canvas, row=row,
                                                     col=col)
                self.grid_locs.add((row, col))

    def animate(self, root):
        # first, add all new particles to the grid (added via mouse)
        self.get_new_particles()
        for i in range(len(self.grid_locs)):
            # choose single random valid location
            if len(self.grid_locs) > 0:
                random_row, random_col = random.choice(tuple(self.grid_locs))
                particle = self.grid[random_row][random_col]
                new_row, new_col = particle.update()
                if self.grid[random_row][random_col] is None:
                    self.grid_locs.remove((random_row, random_col))
                self.grid_locs.add((new_row, new_col))

        self.canvas.update()
        if self.need_to_clear:
            self.clear_particles()
        root.after(FALL_RATE, lambda: self.animate(root))


def main():
    root = Tk()
    root.geometry(str(CANVAS_WIDTH) + "x" +
                  str(CANVAS_HEIGHT) + "+" +
                  str(WINDOW_TOP_X) + "+" +
                  str(WINDOW_TOP_Y))
    root.resizable(False, False)

    playground = Playground()
    Particle.grid = playground.grid

    root.bind('<Motion>', playground.mouse_moved)
    root.bind('<ButtonPress-1>', lambda e: playground.mouse_button(e, True))
    root.bind('<ButtonRelease-1>', lambda e: playground.mouse_button(e, False))

    root.after(1000, lambda: playground.animate(root))
    root.mainloop()


if __name__ == "__main__":
    main()

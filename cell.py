from utils import *


class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._window = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        wall_color = "black"
        blank_wall = "white"
        if self._window is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        line = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self._window.draw_line(line, wall_color)
        else:
            self._window.draw_line(line, blank_wall)

        line = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self._window.draw_line(line, wall_color)
        else:
            self._window.draw_line(line, blank_wall)

        line = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self._window.draw_line(line, wall_color)
        else:
            self._window.draw_line(line, blank_wall)

        line = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self._window.draw_line(line, wall_color)
        else:
            self._window.draw_line(line, blank_wall)

    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._window.draw_line(line, fill_color)

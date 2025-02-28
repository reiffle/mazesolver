from graphics import Point, Line

class Cell:
    def __init__(self, win):
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.wall_left = True
        self.wall_right = True
        self.wall_top = True
        self.wall_bottom = True
        self.win=win

    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        if self.wall_left:
            self.win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        if self.wall_right:
            self.win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        if self.wall_top:
            self.win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        if self.wall_bottom:
            self.win.draw_line(Line(Point(x1, y2), Point(x2, y2)))

    def draw_move(self, to_cell, undo=False):
        start_x = (self.x1 + self.x2) / 2
        start_y = (self.y1 + self.y2) / 2
        end_x = (to_cell.x1 + to_cell.x2) / 2
        end_y = (to_cell.y1 + to_cell.y2) / 2
        self.win.draw_line(Line(Point(start_x, start_y), Point(end_x, end_y)), "gray" if undo else "red")

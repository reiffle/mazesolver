from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height, bg_color="white"):
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.title("Maze Solver")
        self.bg_color = bg_color
        self.canvas = Canvas(self.root, bg=self.bg_color, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
        
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color="black", width=2):
        line.draw(self.canvas, fill_color, width)

class Point:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

class Line:
    def __init__(self, point1=Point, point2=Point):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color="black", width=2):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=width)
            
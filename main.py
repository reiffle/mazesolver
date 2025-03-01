from graphics import Window
from cell import Cell
from maze import Maze

def main():
    win=Window(800, 600)
    num_cols = 10
    num_rows = 12
    m1 = Maze(50, 50, num_rows, num_cols, 50, 50, win)
    m1._break_entrance_and_exit()

    win.wait_for_close()

main()
import time
from graphics import Window
from maze import Maze

def main():
    win_x = 800
    win_y = 800
    num_cols = 20
    num_rows = 20
    cell_x = win_x // (num_cols + 2)
    cell_y = win_y // (num_rows + 2)
    bord_x = cell_x
    bord_y = cell_y
    win=Window(win_x, win_y)
    m1 = Maze(bord_x, bord_y, num_rows, num_cols, cell_x, cell_y, win)
    m1._break_entrance_and_exit()
    m1._break_walls_r(0, 0)
    m1._reset_cells_visited()
    m1.solve()
    win.wait_for_close()

main()
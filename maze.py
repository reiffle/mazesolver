import time, random
from cell import Cell

class Maze:

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
        ):

        self.x1 = x1 # x1 is the x-coordinate of the top-left corner of the maze
        self.y1 = y1 # y1 is the y-coordinate of the top-left corner of the maze
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for cols in range(self.num_cols):
            col = []
            for rows in range(self.num_rows):
                c=Cell(self.win)
                col.append(c)
            self._cells.append(col)
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, i, j):
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        if self.win:
            self._cells[i][j].draw(x1, y1, x2, y2)
            self._animate()

    def _animate(self):
        if self.win:
            self.win.redraw()
            time.sleep(0.02)

    def _break_entrance_and_exit(self):
        self._cells[0][0].wall_left = False
        self._cells[self.num_cols-1][self.num_rows-1].wall_right = False
        self._draw_cell(0, 0)
        self._draw_cell(self.num_cols-1, self.num_rows-1)

    def _break_walls_r (self, i, j):
        self._cells[i][j].visited = True # Mark the cell as visited
        while True:
            # Create a list of possible directions (cells not visited yet)
            possible_directions = []
        
            # Check left
            if i > 0 and not self._cells[i-1][j].visited:
                possible_directions.append(("left", i-1, j))
        
            # Check right
            if i < self.num_cols-1 and not self._cells[i+1][j].visited:
                possible_directions.append(("right", i+1, j))
        
            # Check up
            if j > 0 and not self._cells[i][j-1].visited:
                possible_directions.append(("up", i, j-1))
        
            # Check down
            if j < self.num_rows-1 and not self._cells[i][j+1].visited:
                possible_directions.append(("down", i, j+1))
        
            # If no directions left, draw the cell and return
            if not possible_directions:
                self._draw_cell(i, j)
                return
        
            # Choose a random direction
            choice, new_i, new_j = random.choice(possible_directions)

            if choice == "up" and self._cells[i][j].wall_top:
                self._cells[i][j].wall_top = False
                self._cells[new_i][new_j].wall_bottom = False
            elif choice == "down" and self._cells[i][j].wall_bottom:
                self._cells[i][j].wall_bottom = False
                self._cells[new_i][new_j].wall_top = False
            elif choice == "left" and self._cells[i][j].wall_left:
                self._cells[i][j].wall_left = False
                self._cells[new_i][new_j].wall_right = False
            elif choice == "right" and self._cells[i][j].wall_right:
                self._cells[i][j].wall_right = False
                self._cells[new_i][new_j].wall_left = False
            self._break_walls_r(new_i, new_j) # Recursively call the function with the new coordinates

    def _reset_cells_visited(self):
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self._cells[col][row].visited = False

    def solve (self):
        return self._solve_r(0, 0)
    
    def _solve_r (self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        # Return true if at end of maze
        if i == self.num_cols-1 and j == self.num_rows-1:
            return True
        if i-1>=0 and self._cells[i][j].wall_left is False and self._cells[i-1][j].visited is False:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            self._cells[i-1][j].draw_move(self._cells[i][j], True)
        if i+1<self.num_cols and self._cells[i][j].wall_right is False and self._cells[i+1][j].visited is False:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            self._cells[i+1][j].draw_move(self._cells[i][j], True)
        if j-1>=0 and self._cells[i][j].wall_top is False and self._cells[i][j-1].visited is False:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            self._cells[i][j-1].draw_move(self._cells[i][j], True)
        if j+1<self.num_rows and self._cells[i][j].wall_bottom is False and self._cells[i][j+1].visited is False:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            self._cells[i][j+1].draw_move(self._cells[i][j], True)
        return False
    
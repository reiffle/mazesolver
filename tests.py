import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 10
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 10
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertFalse(m1._cells[0][0].wall_left)
        self.assertFalse(m1._cells[num_cols-1][num_rows-1].wall_right)

if __name__ == "__main__":
    unittest.main()
import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells_uneven(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(5, 5, num_rows, num_cols, 10, 20)

    def test_maze_reset_visited(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._cells[0][0].visited = True
        m1._cells[5][5].visited = True
        m1._cells[9][9].visited = True

        self.assertTrue(m1._cells[0][0].visited)
        self.assertTrue(m1._cells[5][5].visited)
        self.assertTrue(m1._cells[9][9].visited)

        m1._reset_cells_visited()
        for col in m1._cells:
            for cell in col:
                self.assertFalse(cell.visited)


if __name__ == "__main__":
    unittest.main()

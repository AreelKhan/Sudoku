import numpy as np


class SolveSudoku:
    """
    An object that solves a Sudoku using the backtracking algorithm
    """

    def __init__(self, board):
        """
        Instantiation of SolveSudoku Class
        :type board: numpy.ndarray
        """
        self.board = board

    def __str__(self):
        """
        Print the numpy array
        """
        return print(self.board)

    def axis_check(self, x, y, value):
        """
        Checks if a value can is repeated in the row, column, or box of the given x,y coordinate

        :type x: int
        :type y: int
        :type value: int

        Constraints:
        0 <= x,y <= 8
        1 <= value <= 9
        """

        square_x = x // 3
        square_y = y // 3

        # Check row
        if value in self.board[x]:
            return False

        # Check column
        elif value in self.board[:, y]:
            return False

        # Check box
        elif value in self.board[square_x * 3:(square_x + 1) * 3, square_y * 3:(square_y + 1) * 3]:
            return False

        return True

    def find_empty(self):
        """
        Locates the coordinates of cells where the board is empty. (has a value of 0)

        :rtype: list of tuples
        """
        x, y = np.where(self.board == 0)
        list_of_empty = list(zip(x, y))
        return list_of_empty

    def backtrack(self):
        """
        Uses the backtracking algorithm to recursively solve the Sudoku Board.

        :rtype: None (Mutates the self.board attribute)
        """
        empties = self.find_empty()
        if not empties:
            return True  # all cells are non_empty
        x, y = empties[0]

        for candidate in range(1, 10):
            if self.axis_check(x, y, candidate):
                self.board[x, y] = candidate

                if self.backtrack():
                    return True

                self.board[x, y] = 0
        return False


# Testing
if __name__ == "__main__":
    bo = np.array([
        [9, 0, 0, 0, 0, 0, 4, 0, 7],
        [0, 0, 5, 0, 0, 9, 0, 0, 0],
        [8, 0, 3, 0, 6, 0, 0, 0, 0],
        [0, 0, 4, 3, 1, 0, 0, 0, 9],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [6, 0, 0, 0, 9, 5, 1, 0, 0],
        [0, 0, 0, 0, 3, 0, 7, 0, 4],
        [0, 0, 0, 1, 0, 0, 9, 0, 0],
        [3, 0, 8, 0, 0, 0, 0, 0, 5]
    ])
    test = SolveSudoku(bo)
    test.backtrack()
    print(test.board)

import requests
import sys
import numpy as np
import pygame as pg
from solve_sudoku import SolveSudoku

# Define initial variables

# Width of Pygame screen
width = 550

# Background color of screen
background_color = (225, 225, 225)

# Color of hints
hint_color = (0, 0, 0)

# A buffer defined to adjust aesthetics
buffer = 5

# Name of the window created
app_name = "SUDOKU"

# An API that provides random Sudoku Boards
api_response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = np.array(api_response.json()["board"])
original_grid = grid.copy()


def display_solved(win):
    """
    Displays the solved board.
    Takes grid values from original_grid, which is mutated by SudokuSolver

    :type win: pygame.Surface
    :rtype: None
    """
    SolveSudoku(original_grid).backtrack()
    solved_font = pg.font.SysFont("arial", 35)
    pg.draw.rect(win, background_color,(0, 0, width, width))
    for i in range(10):
        line_width = 4 if i % 3 == 0 else 2
        pg.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), line_width)
        pg.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), line_width)

    for i in range(9):
        for j in range(9):
            number = solved_font.render(str(original_grid[i, j]), True, hint_color)
            win.blit(number, ((j + 1) * 50 + 18, (i + 1) * 50 + 5))
        pg.display.update()


def interact(win, coordinate):
    """
    Enters a value in the a given position of the board

    :type win: pygame.Surface
    :type coordinate: tuple of int
    """
    j, i = coordinate
    entry_font = pg.font.SysFont("arial", 35)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if original_grid[i - 1, j - 1] != 0:
                    return
                if event.key == 8:
                    grid[i - 1][j - 1] = 0
                    pg.draw.rect(win, background_color, (
                        coordinate[0] * 50 + buffer, coordinate[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                    pg.display.update()
                    return
                if 0 < event.key - 48 < 10:
                    pg.draw.rect(win, background_color, (
                        coordinate[0] * 50 + buffer, coordinate[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))

                    entry = entry_font.render(str(event.key - 48), True, (25, 150, 250))
                    win.blit(entry, (coordinate[0] * 50 + 18, coordinate[1] * 50 + 5))
                    grid[i - 1][j - 1] = event.key - 48
                    pg.display.update()
                    return
                return


def main():
    """
    Instanties Pygame, produces Sudoku

    """
    pg.init()
    window = pg.display.set_mode((width, width))
    pg.display.set_caption(app_name)
    window.fill(background_color)
    font = pg.font.SysFont("arial", 35)

    for i in range(10):
        line_width = 4 if i % 3 == 0 else 2
        pg.draw.line(window, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), line_width)
        pg.draw.line(window, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), line_width)

    for i in range(9):
        for j in range(9):
            if grid[i, j] != 0:
                number = font.render(str(grid[i, j]), True, hint_color)
                window.blit(number, ((j + 1) * 50 + 18, (i + 1) * 50 + 5))
    pg.display.update()

    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == 115:
                    display_solved(window)
            if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                cursor_position = pg.mouse.get_pos()
                interact(window, (cursor_position[0] // 50, cursor_position[1] // 50))
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()


main()

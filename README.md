# Sudoku
A **Sudoku puzzle** and integrated **Sudoku Solver** written using Pygame

## Background:
This project started off as an attempt at answering [Leetcode 37. Sudoku Solver.](https://leetcode.com/problems/sudoku-solver/) 

I solved the problem using the Backtracking algorithm. Although I thought of many algorithms to solve a Sudoku board, the backtracking algorithm seemed the most efficient,
elegant and easy to implement.

## Description:
There are two parts to this project. The sudoku game and the sudoku solver. The frontend is fairly simple, with the GUI of the game designed using a module called Pygame. In the backend, a request to the sugoku API generates a random sudoku board. The game is stored as a 2D array. The user can make inputs using the keyboard and mouse. When the use presses enter s on the keyboard. A solved version of the sudoku board is displayed. 

## How to play:

1. Run the SudokuGame.py file.
2. A Sudoku GUI will pop-up
3. Enter a value by left-clicking the square and entering an integer from 1-9 inclusive.
4. If you want to see the solution, press s on the keyboard.

Example of an empty Board

<img width="412" alt="Board" src="https://user-images.githubusercontent.com/76454082/114672723-7337c780-9cd3-11eb-8264-98107de57558.png">

Example of user inputs

<img width="412" alt="Inputs" src="https://user-images.githubusercontent.com/76454082/114673164-e7726b00-9cd3-11eb-80c6-b669c6ce217d.png">

Example of a solved Board

<img width="412" alt="Solved" src="https://user-images.githubusercontent.com/76454082/114672730-75018b00-9cd3-11eb-8765-4bf9df50a980.png">

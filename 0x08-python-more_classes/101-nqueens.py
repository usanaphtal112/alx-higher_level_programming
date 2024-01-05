#!/usr/bin/python3
"""
N-Queens Solver.

This script implements a recursive solution to the N-Queens problem.
Given a positive integer N, it finds all possible
solutions to placing N queens on an NxN chessboard
such that no two queens threaten each other.

Usage:
    $ python script_name.py N

    N: The size of the chessboard (positive integer >= 4)

Example:
    $ python script_name.py 4
"""
import sys


def init_board(n):
    """
    Initialize an empty NxN chessboard.

    Parameters:
        n (int): The size of the chessboard.

    Returns:
        list: An empty NxN chessboard represented as a 2D list.
    """
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """
    Create a deep copy of the chessboard.

    Parameters:
        board (list): The chessboard to be copied.

    Returns:
        list: A deep copy of the chessboard.
    """
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """
    Extract the positions of queens from the chessboard.

    Parameters:
        board (list): The chessboard.

    Returns:
        list: A list of positions (row, col) where queens are placed.
    """
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(board, row, col):
    """
    Mark the threatened positions on the chessboard after placing a queen.

    Parameters:
        board (list): The chessboard.
        row (int): The row where the queen is placed.
        col (int): The column where the queen is placed.
    """
    # X out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """
    Recursively solve the N-Queens problem and find all possible solutions.

    Parameters:
        board (list): The chessboard.
        row (int): The current row.
        queens (int): The number of queens placed so far.
        solutions (list): List to store found solutions.

    Returns:
        list: List of solutions, each containing the positions of queens.
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)

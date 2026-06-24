#!/usr/bin/python3
"""N Queens - solve the N queens puzzle."""
import sys


def is_safe(queens, row, col):
    """Return True if placing a queen at (row, col) is safe."""
    for r, c in queens:
        if r == row or c == col:
            return False
        if abs(r - row) == abs(c - col):
            return False
    return True


def solve_nqueens(n, queens=None, col=0):
    """Print all solutions for the N queens puzzle."""
    if queens is None:
        queens = []
    if col == n:
        print(queens)
        return
    for row in range(n):
        if is_safe(queens, row, col):
            solve_nqueens(n, queens + [[row, col]], col + 1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_nqueens(n)

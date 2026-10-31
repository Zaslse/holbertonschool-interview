#!/usr/bin/python3
"""Solve the N queens problem using backtracking."""

import sys


def solve_nqueens(n):
    """Print all valid arrangements of N non-attacking queens."""
    columns = set()
    diagonals_down = set()
    diagonals_up = set()
    solution = []

    def backtrack(row):
        """Place queens recursively, one queen per row."""
        if row == n:
            print([[r, c] for r, c in enumerate(solution)])
            return

        for col in range(n):
            down = row - col
            up = row + col

            if (col in columns or
                    down in diagonals_down or
                    up in diagonals_up):
                continue

            columns.add(col)
            diagonals_down.add(down)
            diagonals_up.add(up)
            solution.append(col)

            backtrack(row + 1)

            solution.pop()
            columns.remove(col)
            diagonals_down.remove(down)
            diagonals_up.remove(up)

    backtrack(0)


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

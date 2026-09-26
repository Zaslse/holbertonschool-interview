#!/usr/bin/python3
"""Pascal's Triangle module."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]

        if i > 0:
            previous = triangle[i - 1]

            for j in range(1, i):
                row.append(previous[j - 1] + previous[j])

            row.append(1)

        triangle.append(row)

    return triangle

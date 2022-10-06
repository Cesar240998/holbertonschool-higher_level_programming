#!/usr/bin/python3
"""Module 14-pascal_triangle.
Returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.
    """

    if n <= 0:
        return []

    lis = [[0 for x in range(i + 1)] for i in range(n)]
    lis[0] = [1]

    for i in range(1, n):
        lis[i][0] = 1
        for j in range(1, i + 1):
            if j < len(lis[i - 1]):
                lis[i][j] = lis[i - 1][j - 1] + lis[i - 1][j]
            else:
                lis[i][j] = lis[i - 1][0]
            return lis

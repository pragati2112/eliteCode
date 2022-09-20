'''
https://leetcode.com/problems/01-matrix/

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
'''


def update_matrix(mat):
    rows = len(mat)
    columns = len(mat[0])

    visited = {}
    queue = []

    result = [[float('inf') for i in range(columns)] for j in range(rows)]

    for row in range(rows):
        for column in range(columns):
            if mat[row][column] == 0:
                result[row][column] = 0
                queue.append([row, column])

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while len(queue) > 0:
        row, column = queue.pop(0)
        distance = result[row][column]
        for direction in directions:
            new_row = row + direction[0]
            new_column = column + direction[1]

            if 0 <= new_row < rows and 0 <= new_column < columns:
                if result[new_row][new_column] > 1 + distance:
                    result[new_row][new_column] = 1 + distance
                    queue.append([new_row, new_column])
    return result


print(update_matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(update_matrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))

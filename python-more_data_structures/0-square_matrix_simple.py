#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(0, len(matrix)):
        new_row = []
        for j in range(0, len(matrix[0])):
            new_row.append(pow(matrix[i][j], 2))
        new_matrix.append(new_row)
    return new_matrix
    # return [[element**2 for element in row] for row in matrix]

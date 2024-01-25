#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if j != len(matrix[i]) - 1:
                print("{:d} ".format(matrix[i][j]), end="")
            else:
                print("{:d}".format(matrix[i][j]), end="")
        print()


# for row in matrix:
#         for el in row:
#             if el != row[-1]:
#                 print("{:d}".format(el), end=" ")
#             else:
#                 print("{:d}".format(el), end="")

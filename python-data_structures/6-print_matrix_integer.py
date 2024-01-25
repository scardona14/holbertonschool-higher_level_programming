#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers"""
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end="")
            if col != row[-1]:
                print(" ", end="")
        print("")

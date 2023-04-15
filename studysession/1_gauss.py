'''
Tip: get examples from
https://www.cliffsnotes.com/study-guides/algebra/linear-algebra/linear-systems/gaussian-elimination
'''

import numpy as np

def print_shape(matrix_a, matrix_b):
    print("Matrix A:")
    print(f"\tShape[0] = {matrix_a.shape[0]}")
    print(f"\tShape[1] = {matrix_a.shape[1]}")
    print("Matrix B:")
    print(f"\tShape[0] = {matrix_b.shape[0]}")
    print(f"\tShape[1] = {matrix_b.shape[1]}")

def gauss_elimination(matrix_a, matrix_b):

    # Validation
    if matrix_a.shape[0] != matrix_a.shape[1]:
        print("Error: A matrix is not square")
        return
    
    if matrix_b.shape[1] > 1 or matrix_b.shape[0] != matrix_a.shape[0]:
        print("Error: shape of B matrix is invalid")
        return

    # Create augmented matrix
    augmented_matrix = np.concatenate((matrix_a, matrix_b), axis=1, dtype=float)
    print("\nOriginal augmented matrix:")
    print(augmented_matrix)

    # Obtaining the upper-triangular matrix
    print("\nObtaining upper-triangular matrix")
    n = len(augmented_matrix)   # number of rows
    for i in range(n):
        if augmented_matrix[i][i] == 0:
            print("\nError: there is a zero at the main diagonal")
            return
        for j in range(i+1, n):
            scaling_factor = augmented_matrix[j][i]/ augmented_matrix[i][i]
            augmented_matrix[j] = augmented_matrix[j] - augmented_matrix[i]*scaling_factor
            print(augmented_matrix)

    # Backwards substitution
    m = n-1
    s = np.zeros(n)
    print("\nObtaining solution vector:")
    print(s)
       
    for i in range(n-1, -1, -1):        # For each line, bottom up
        numerator = augmented_matrix[i][n]

        for j in range(i+1, n):         # For each valid collum, left to right
            numerator -= augmented_matrix[i][j] * s[j]

        s[i] = numerator / augmented_matrix[i][i]

        print(s)

    # Print answer
    print()
    for answer in range(n):
        print(f"x{answer} is: {s[answer]}")


variables_matrix = np.array([[1, -2, 1], [2, 1, -3], [4, -7, 1]])
constants_matrix = np.array([[0], [5], [-1]])
# variables_matrix = np.array([[2, -2, 0], [1, -1, 1], [0, 3, -2]])
# constants_matrix = np.array([[-6], [1], [-5]])

gauss_elimination(variables_matrix, constants_matrix)
from sympy import Matrix 

A = [
        [1, 2, 3],
        [4, 1, 6],
        [7, 8, 1]
    ]

A = Matrix(A)
det_A = A.det() #determinant of A

print("det_A:", det_A)

"""
det_A: 104
"""

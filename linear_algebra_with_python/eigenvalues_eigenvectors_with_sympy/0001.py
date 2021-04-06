from sympy import Matrix, pprint, Eq

A = [
        [ 1, 1, 1],
        [ 1, 0, 1],
        [ 1, 1, 1]
    ]

A = Matrix(A)

print("A:")
pprint(A)
print("--------------------------1------------------------------")

eigenvalues = A.eigenvals() #returns the engenvalues of A in the form of a dictionary
                            #{eigenvalue_1: multiplicity_1, eigenvalue_2: multiplicity_2, eigenvalue_3: multiplicity_3}
print("the eigenvalues and their multiplicities are:")
print("eigenvalues:") 
pprint(eigenvalues)

print("--------------------------2------------------------------")

eigenvectors = A.eigenvects() #returns the eigenvectors of A in the form of a list of tuples
print("the eigenvalues, multiplicities, and eigenvectors are:")
print("eigenvectors:")
pprint(eigenvectors)

print("--------------------------3------------------------------")

k = list(eigenvalues) #convert the dictionary into a list
print("k:")
pprint(k)

print("--------------------------4------------------------------")

#eigenvalues 
k_1 = k[0] 
k_2 = k[1] 
k_3 = k[2]
print("k_1:", k_1)
print("k_2:", k_2)
print("k_3:", k_3)

print("--------------------------5------------------------------")

#get the list of tuples as individual list of lists
x_1 = eigenvectors[0][2]
x_2 = eigenvectors[1][2]
x_3 = eigenvectors[2][2]

#convert the list of lists into individual lists

#eigenvectors
x_1 = x_1[0] 
x_2 = x_2[0] 
x_3 = x_3[0]

print("x_1:")
pprint(x_1)
print()
print("x_2:")
pprint(x_2)
print()
print("x_3:")
pprint(x_3)

print("---------------------------6-----------------------------")

print("verify the solution")
print("check if Ax = kx is true for all k and x pairs")

#x is the set of eigenvectors
#k is the set of eigenvalues

#There is no ordering for the eigenvalues and eigenvectors.
#Therefore, we must try all possible multiplications.

print("---------------------------7-----------------------------")

x = [x_1, x_2, x_3]
k = [k_1, k_2, k_3]

num_x = len(x)
num_k = len(k)

for i in range(0, num_k):
    for j in range(0, num_x): 
        lhs = A * x[i]
        rhs = k[j] * x[i]
        if(Eq(lhs, rhs)):
            print("The eigenvalue")
            pprint(k[j])
            print("and the eigenvector")
            pprint(x[i])
            print("form a pair of eigenvalue-eigenvector that solves the system.")
            print("-------------------------------------------------------------")

"""
A:
⎡1  1  1⎤
⎢       ⎥
⎢1  0  1⎥
⎢       ⎥
⎣1  1  1⎦
--------------------------1------------------------------
the eigenvalues and their multiplicities are:
eigenvalues:
{0: 1, 1 - √3: 1, 1 + √3: 1}
--------------------------2------------------------------
the eigenvalues, multiplicities, and eigenvectors are:
eigenvectors:
⎡                ⎛           ⎡⎡    1     ⎤⎤⎞  ⎛           ⎡⎡     1     ⎤⎤⎞⎤
⎢⎛      ⎡⎡-1⎤⎤⎞  ⎜           ⎢⎢          ⎥⎥⎟  ⎜           ⎢⎢           ⎥⎥⎟⎥
⎢⎜      ⎢⎢  ⎥⎥⎟  ⎜           ⎢⎢-(1 - √3) ⎥⎥⎟  ⎜           ⎢⎢-(-√3 - 1) ⎥⎥⎟⎥
⎢⎜0, 1, ⎢⎢0 ⎥⎥⎟, ⎜1 - √3, 1, ⎢⎢──────────⎥⎥⎟, ⎜1 + √3, 1, ⎢⎢───────────⎥⎥⎟⎥
⎢⎜      ⎢⎢  ⎥⎥⎟  ⎜           ⎢⎢ -2 + √3  ⎥⎥⎟  ⎜           ⎢⎢   √3 + 2  ⎥⎥⎟⎥
⎢⎝      ⎣⎣1 ⎦⎦⎠  ⎜           ⎢⎢          ⎥⎥⎟  ⎜           ⎢⎢           ⎥⎥⎟⎥
⎣                ⎝           ⎣⎣    1     ⎦⎦⎠  ⎝           ⎣⎣     1     ⎦⎦⎠⎦
--------------------------3------------------------------
k:
[1 - √3, 1 + √3, 0]
--------------------------4------------------------------
k_1: 1 - sqrt(3)
k_2: 1 + sqrt(3)
k_3: 0
--------------------------5------------------------------
x_1:
⎡-1⎤
⎢  ⎥
⎢0 ⎥
⎢  ⎥
⎣1 ⎦

x_2:
⎡    1     ⎤
⎢          ⎥
⎢-(1 - √3) ⎥
⎢──────────⎥
⎢ -2 + √3  ⎥
⎢          ⎥
⎣    1     ⎦

x_3:
⎡     1     ⎤
⎢           ⎥
⎢-(-√3 - 1) ⎥
⎢───────────⎥
⎢   √3 + 2  ⎥
⎢           ⎥
⎣     1     ⎦
---------------------------6-----------------------------
verify the solution
check if Ax = kx is true for all k and x pairs
---------------------------7-----------------------------
The eigenvalue
0
and the eigenvector
⎡-1⎤
⎢  ⎥
⎢0 ⎥
⎢  ⎥
⎣1 ⎦
form a pair of eigenvalue-eigenvector that solves the system.
-------------------------------------------------------------
The eigenvalue
1 - √3
and the eigenvector
⎡    1     ⎤
⎢          ⎥
⎢-(1 - √3) ⎥
⎢──────────⎥
⎢ -2 + √3  ⎥
⎢          ⎥
⎣    1     ⎦
form a pair of eigenvalue-eigenvector that solves the system.
-------------------------------------------------------------
The eigenvalue
1 + √3
and the eigenvector
⎡     1     ⎤
⎢           ⎥
⎢-(-√3 - 1) ⎥
⎢───────────⎥
⎢   √3 + 2  ⎥
⎢           ⎥
⎣     1     ⎦
form a pair of eigenvalue-eigenvector that solves the system.
-------------------------------------------------------------
"""

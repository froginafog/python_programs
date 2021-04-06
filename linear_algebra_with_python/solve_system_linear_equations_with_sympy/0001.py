from sympy import Matrix, pprint, linsolve, Symbol, Eq

"""
solve Ax = b

example

1 * x_1 + 2 * x_2 - 3 * x_3 - 4 * x_4 = -2
1 * x_1 - 3 * x_2 + 2 * x_3 + 6 * x_4 =  4
3 * x_1 - 1 * x_2 + 3 * x_3 + 2 * x_4 =  2
2 * x_1 + 3 * x_2 + 2 * x_3 - 2 * x_4 = -4
"""

x_1 = Symbol('x_1')
x_2 = Symbol('x_2')
x_3 = Symbol('x_3')
x_4 = Symbol('x_4')

lhs_eq_1 =  1 * x_1 + 2 * x_2 - 3 * x_3 - 4 * x_4
lhs_eq_2 =  1 * x_1 - 3 * x_2 + 2 * x_3 + 6 * x_4
lhs_eq_3 =  3 * x_1 - 1 * x_2 + 3 * x_3 + 2 * x_4
lhs_eq_4 =  2 * x_1 + 3 * x_2 + 2 * x_3 - 2 * x_4

rhs_eq_1_value = -2
rhs_eq_2_value =  4
rhs_eq_3_value =  2
rhs_eq_4_value = -4

eq_1 = Eq(lhs_eq_1, rhs_eq_1_value)
eq_2 = Eq(lhs_eq_2, rhs_eq_2_value)
eq_3 = Eq(lhs_eq_3, rhs_eq_3_value)
eq_4 = Eq(lhs_eq_4, rhs_eq_4_value)

x = linsolve([eq_1, eq_2, eq_3, eq_4], (x_1, x_2, x_3, x_4))
#x = {[x_1, x_2, x_3, x_4]}
#The type of x is <class 'sympy.sets.sets.FiniteSet'>

x = list(x) #convert to list

x = x[0] #the first set of the list is the solution that we want

print("solution x:")
pprint(Matrix(x))
print()

#substitute the values into the LHS of the equation
lhs_eq_1_value = lhs_eq_1.subs({x_1: x[0], x_2: x[1], x_3: x[2], x_4: x[3]})
lhs_eq_2_value = lhs_eq_2.subs({x_1: x[0], x_2: x[1], x_3: x[2], x_4: x[3]})
lhs_eq_3_value = lhs_eq_3.subs({x_1: x[0], x_2: x[1], x_3: x[2], x_4: x[3]})
lhs_eq_4_value = lhs_eq_4.subs({x_1: x[0], x_2: x[1], x_3: x[2], x_4: x[3]})

print("lhs_eq_1_value:", lhs_eq_1_value)
print("lhs_eq_2_value:", lhs_eq_2_value)
print("lhs_eq_3_value:", lhs_eq_3_value)
print("lhs_eq_4_value:", lhs_eq_4_value)

print()

print("rhs_eq_1_value:", rhs_eq_1_value)
print("rhs_eq_2_value:", rhs_eq_2_value)
print("rhs_eq_3_value:", rhs_eq_3_value)
print("rhs_eq_4_value:", rhs_eq_4_value)

print()

print("The solution x:")
pprint(Matrix(x))

#check the solution
if(lhs_eq_1_value == rhs_eq_1_value and lhs_eq_2_value == rhs_eq_2_value and lhs_eq_3_value == rhs_eq_3_value and lhs_eq_4_value == rhs_eq_4_value):
    print("is correct.")
else:
    print("is incorrect.")

"""
solution x:
⎡8/25 ⎤
⎢     ⎥
⎢-8/5 ⎥
⎢     ⎥
⎢-2/25⎥
⎢     ⎥
⎣-4/25⎦

lhs_eq_1_value: -2
lhs_eq_2_value: 4
lhs_eq_3_value: 2
lhs_eq_4_value: -4

rhs_eq_1_value: -2
rhs_eq_2_value: 4
rhs_eq_3_value: 2
rhs_eq_4_value: -4

The solution x:
⎡8/25 ⎤
⎢     ⎥
⎢-8/5 ⎥
⎢     ⎥
⎢-2/25⎥
⎢     ⎥
⎣-4/25⎦
is correct.
"""

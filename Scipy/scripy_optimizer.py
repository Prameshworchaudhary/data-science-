#Optimizers are a set of procedures defined in SciPy that either find the minimum value of a function, or the root of an equation.

"""NumPy is capable of finding roots for polynomials and linear equations, but it can not find roots for non linear equations, like this one:

x + cos(x)

For that you can use SciPy's optimze.root function.

This function takes two required arguments:

fun - a function representing an equation.

x0 - an initial guess for the root.

The function returns an object with information regarding the solution.

The actual solution is given under attribute x of the returned object:"""

#Find root of the equation x + cos(x):
from scipy.optimize import root
from math import cos

def equ(x):
    return x + cos(x)
output=root(equ,0)
print(output.x)

def equ(x):
    return (2*x**4-9*x**3-21*x**2 + 88*x + 48)
output=root(equ,0)
print(output.x)
# import cmath
import cmath

def complex_sqrt(z):
    return cmath.sqrt(z)

# Example usage:
result = complex_sqrt(3 + 4j)
print("Square root:", result)

#finding minima
"""We can use scipy.optimize.minimize() function to minimize the function.

The minimize() function takes the following arguments:

fun - a function representing an equation.

x0 - an initial guess for the root.

method - name of the method to use. Legal values:"""

from scipy.optimize import minimize

def eqn(x):
  return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS')

print(mymin)

# #from scipy.optimize import maxi

# def eqn(x):
#   return x**2 + x + 2

# mymax= maximize(eqn, 0, method='BFGS')

# print(mymax)
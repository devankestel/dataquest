## 4. Limits Using SymPy ##

import sympy
x2,y = sympy.symbols('x2 y')
fx2 = -(2.9**2) + 3*2.9 -1
limit_one = sympy.limit((
                        (fx2 + 1)/(x2 -3)), x2, 2.9)
print(limit_one)

## 5. Properties Of Limits I ##

import sympy
x,y = sympy.symbols('x y')
limit_sq = sympy.limit(3*x**2, x, 1)
limit_lin = sympy.limit(3*x, x, 1)
limit_const = -3
limit_two = limit_sq + limit_lin + limit_const
print(limit_two)

## 6. Properties Of Limits II ##

import sympy
x,y = sympy.symbols('x y')
lim_cubed = sympy.limit(x**3, x, -1)
lim_sq = 2*sympy.limit(x**2, x, -1)
lim_lin = 10*sympy.limit(x, x, -1)
limit_three = lim_cubed + lim_sq - lim_lin
print(limit_three)

## 7. Undefined Limit To Defined Limit ##

import sympy
x2, y = sympy.symbols('x2 y')
limit_four = sympy.limit(-x, x, 3)
print(limit_four)
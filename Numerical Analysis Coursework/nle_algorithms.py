# -*- coding: utf-8 -*-
"""NLE_algorithms.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AaqtBOt9Ec0YzS6tDahoJ5QXvHYRUtyq
"""

import math
import numpy as np
from tabulate import tabulate

"""Write a python script to implement the ***bisection method***."""

def bisection(f, a, b, tol):
  if f(a)*f(b) > 0:
    print("Error: endpoints have same sign")
    return
  while (b-a) > tol:
    c = (a+b)/2
    if f(c)*f(a) < 0:
      b = c
    elif f(c)*f(a) > 0:
      a = c
    elif f(c) < 10**(-16): #c is the root
      return c
  return (a+b)/2

"""

*   Estimate √5 to 8 decimal places



"""

f = lambda x: x**2 - 5
a, b = 1, 3
tol = 0.5*10**(-8)
xc = bisection(f, a, b, tol)

print(xc)
print(abs(xc - math.sqrt(5)))

"""Write a python script to implement the ***fixed point iteration method***."""

def FPI(g, x0, tol):
  x = x0
  diff = 1
  while diff > tol:
    xnew = g(x)
    diff = abs(xnew - x)
    x = xnew
  return x

g = lambda x: np.cos(x) - np.sin(x) + x
x0 = 1
tol = 10**(-8)
F = FPI(g, x0, tol)
print(F)
print(abs(F - (np.pi/4)))

"""Write a python script to implement ***Newton's method***."""

def newton(f, fp, x0, tol):
  x = x0
  diff = 1
  while diff > tol:
    xnew = x - f(x)/fp(x)
    diff = abs(xnew - x)
    x = xnew
  return x

f = lambda x: math.cos(x) - math.sin(x)
fp = lambda x: -math.sin(x) - math.cos(x)
x0 = 1
tol = 10**(-8)
N = newton(f, fp, x0, tol)
print(N)
print(abs(N - (math.pi/4)))

"""Write a Python script to implement the ***regula falsi method***."""

def regulaFalsi(f, a, b, tol):
  if f(a)*f(b) > 0:
    print("Error: f(a) and f(b) have the same sign")
    return
  while b-a > tol:
    c = ((b*f(a))-(a*f(b)))/(f(a)-f(b))
    if f(c)*f(a) < 0:
      b = c
    elif f(c)*f(a) > 0:
      a = c
    elif f(c) < 10**(-16):
      return c
  return ((b*f(a))-(a*f(b)))/(f(a)-f(b))

"""Write a Python script to implement the ***secant method***."""

def secant(f, xb, xa, tol):
  if f(xb) - f(xa) == 0:
    print("Error: denominator is 0")
    return
  while xa - xb > tol:
    xc = xb - ((f(xb)*(xb-xa))/(f(xb)-f(xa)))
    if f(xc)*f(xb) < 0:
      xa = xc
    elif f(xc)*f(xc) > 0:
      xb = xc
    elif f(xc) < 10**(-16):
      return xc
  return xb - ((f(xb)*(xb-xa))/(f(xb)-f(xa)))

"""

Errors ---

"""

def FPI_error(g, x0, tol):
  approx = []
  x = x0
  diff = 1
  count = 0
  approx.append([count, x, diff])
  while diff > tol:
    xnew = g(x)
    diff = abs(xnew - x)
    x = xnew
    count += 1
    approx.append([count, x, diff])
  return approx

def newton_error(f, fp, x0, tol):
  approx = []
  x = x0
  diff = 1
  count = 0
  approx.append([count, x, diff])
  while diff > tol:
    xnew = x - f(x)/fp(x)
    diff = abs(xnew - x)
    x = xnew
    count += 1
    approx.append([count, x, diff])
  return approx

A = FPI_error(g, x0, tol)
print(tabulate(A, headers=["Iteration", "Approximation", "Difference"], floatfmt=".12f"))

B = newton_error(f, fp, x0, tol)
print(tabulate(B, headers=["Iteration", "Approximation", "Difference"], floatfmt=".12f"))
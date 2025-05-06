import math
def sqrt(a):
 if a < 0:
 raise ValueError("Square root of negative number is imaginary.")
 return math.sqrt(a)
def power(a, b):
 return math.pow(a, b)
def log(a, base=10):
 if a <= 0:
 raise ValueError("Logarithm of non-positive number is undefined.")
 return math.log(a, base)
def sine(degrees):
 return math.sin(math.radians(degrees))
def cosine(degrees):
 return math.cos(math.radians(degrees))
def tangent(degrees):
 return math.tan(math.radians(degrees))

import math
def add(a, b):
 return a + b
def sub(a, b):
 return a - b
def multiply(a, b):
 return a * b
def division(a, b):
 if b == 0:
 raise ValueError("Cannot divide by zero.")
 return a / b
def floor_division(a, b):
 if b == 0:
 raise ValueError("Cannot divide by zero.")
 return a // b
def mod(a, b):
 if b == 0:
 raise ValueError("Cannot modulo by zero.")
 return a % b
def power(a, b):
 return math.pow(a, b)

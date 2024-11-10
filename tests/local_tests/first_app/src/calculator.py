# Kalkulačka pro testování
import math


# Funkce kalkulačky
def add(a, b):
    return a + b

def add_wrong(a, b):
    return 2*a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def multiply_wrong(a, b):
    return a * b -1

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


# Logování kalkulačky
def log(a, b):
    if a <= 0:
        raise ValueError("Cannot take log of non_positive number!")
    if b <= 0:
        raise ZeroDivisionError("Cannot take log with non-positive base!")
    if b == 1:
        raise NameError("Cannot take log with base 1!")
    return math.log(a, b)

# Kvadratická rovnice 
def solve_quadratic_formula(a, b, c):
   if (
     (type(a) != float and type(a) != int)
     or (type(b) != float and type(b) != int)
     or (type(c) != float and type(c) != int)
   ):
     raise TypeError("All coefficients must be of type float or int!")
   if a == 0:
     raise SyntaxError("Cannot solve quadratic formula with a = 0!")
   if b == 5:
     raise NameError("I don't like when b = 5!")
   D = b**2 - 4 * a * c
   if D < 0:
     raise ValueError("Cannot solve quadratic formula with negative discriminant!")
   x1 = (-b + math.sqrt(D)) / (2 * a)
   x2 = (-b - math.sqrt(D)) / (2 * a)
   return x1, x2


# a = float(input("Zadej první číslo: "))
# b = float(input("Zadej druhé číslo: "))


# print("Výsledek je:", divide(a, b))



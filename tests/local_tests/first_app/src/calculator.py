# Kalkulačka pro testování

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



# a = float(input("Zadej první číslo: "))
# b = float(input("Zadej druhé číslo: "))


# print("Výsledek je:", divide(a, b))



def addition (x, y):
    return x + y

def div(x, y):
    try:
         return x / y
    except ZeroDivisionError:
         return ("Not allowed!")

def sub (x, y):
    return x - y

def mult (x, y):
    return x * y
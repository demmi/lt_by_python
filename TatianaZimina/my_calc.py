def add(x,y):
    return x+y

def minus(x, y):
    return x-y

def multi(x,y):
    return x*y

def divide(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Can't divide by zero"
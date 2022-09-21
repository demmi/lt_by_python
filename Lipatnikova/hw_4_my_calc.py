def summa(a, b):
    return a + b

def difference(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def subtraction(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Деление на ноль запрещено!"

def degree (a, b):
    return a ** b
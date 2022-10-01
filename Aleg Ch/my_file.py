def sum_it(x, y):
    return x + y


def prod(x, y):
    return x * y


def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("- Can't divide by zero")



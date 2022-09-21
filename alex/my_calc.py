def sum_(a, b):
    return a + b


def sub_(a, b):
    return a - b


def mul_(a, b):
    return a * b


def div_(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        return repr(ex)


def pow_(a, b):
    return a**b

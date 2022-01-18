import numbers

def func(*args):
    result = 0
    for n in args:
        if isinstance(n, numbers.Number):
            result = result+n
    return result
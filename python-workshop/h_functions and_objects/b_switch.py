"""Switch example with function references.
"""
def answer(arg):
    if arg > 42:
        func = return_higher
    elif arg < 42:
        func = return_lower
    else:
        func = return_42
    return func(arg)

def return_42(value):
    return '%s is 42!' % value

def return_lower(value):
    return '%s is lower than 42.' % value

def return_higher(value):
    return '%s is higher than 42.' % value

if __name__ == '__main__':
    print __doc__
    print answer(23)
    print answer(666)
    print answer(42)

"""Functions
"""
def ham():
    pass

def area(x, y):
    return '%s qm' % str(x * y)

def myfunc(*args, **kwargs):
    print type(args)
    print args
    print type(kwargs)
    print kwargs

if __name__ == '__main__':
    print __doc__
    print ham()
    print '-' * 40
    print area(5, 20)
    print area(y= 20, x=3)
    rectangle = area
    print rectangle(20, 30)
    print rectangle
    print '-' * 40
    myfunc(True, 42, 'fruits', order='desc', kind='music')

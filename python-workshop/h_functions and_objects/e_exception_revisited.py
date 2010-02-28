"""Extending and handling exceptions.
"""
class MyError(Exception):
    def __init__(self, value, *args):
        self.value = value
        self.args = args
    
    def __str__(self):
        return repr(self.value)


if __name__ == '__main__':
    print __doc__
    try:
        raise MyError('Something went wrong.', 2, 4)
    except SyntaxError:
        print 'Syntax error'
    except MyError as e:
        print 'My exception says:', e
        raise
    print 'This text will never be shown.'

"""Tuple
"""
paul = ('Paul Pommes', 'Hamburg', '040 1234567')
paul2 = 'Paul Pommes', 'Hamburg', '040 1234567'

if __name__ == '__main__':
    print __doc__
    print paul
    print paul2
    print paul == paul2 # True
    print paul + ('Deutschland',)
    print paul + ('Deutschland') # Will raise a TypeError

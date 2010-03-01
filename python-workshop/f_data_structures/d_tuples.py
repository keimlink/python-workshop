"""Tuple
"""
empty = ()
paul = ('Paul Pommes', 'Hamburg', '040 1234567')
paul2 = 'Paul Pommes', 'Hamburg', '040 1234567'

if __name__ == '__main__':
    print __doc__
    print empty
    print paul
    print paul2
    print paul == paul2 # True
    print paul + ('Deutschland',)
    print paul[1]
    paul[1] = 'Bochum' # Will raise a TypeError

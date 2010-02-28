"""while statement
"""
print __doc__
x = 2
while x < 1000000:
    print x,
    x = x ** 2
# prints 2 4 16 256 65536
print '\n', '-' * 40
while True:
    try:
        x = raw_input('Please enter an integer: ')
        x = int(x)
        break
    except ValueError:
        print 'This is not an integer!'

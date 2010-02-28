"""if statement
"""
print __doc__
x = range(0, 6)
print x
print '-' * 40
if 2 in x:
    print 'Found.'
print '-' * 40
if 7 in x:
    print 'Found.'
else:
    print 'Not found.'
print '-' * 40
if 7 in x:
    print 'Found.'
elif sum(x) > 7:
    print 'Sum is bigger than seven.'
else:
    print 'Not found.'

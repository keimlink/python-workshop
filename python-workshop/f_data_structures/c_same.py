"""The difference between "==" and "is".
"""
print __doc__
a = range(3)
print 'a', a
b = range(3)
print 'b', b
print 'a == b', a == b
print 'a is b', a is b
c = b
print 'c', c
print 'c == b', c == b
print 'c is b', c is b
c.append(4)
print 'c', c
print 'b', b
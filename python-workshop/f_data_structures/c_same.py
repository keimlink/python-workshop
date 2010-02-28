"""The difference between "==" and "is".
"""
print __doc__
a = range(3)
print a
b = range(3)
print b
print a == b
print a is b
c = b
print c
print c == b
print c is b
